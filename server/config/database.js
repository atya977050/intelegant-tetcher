import pkg from 'pg';
import dotenv from 'dotenv';
import os from 'os';
dotenv.config();

const { Pool } = pkg;
const dbUser = process.env.USER || os.userInfo().username;
const connectionString = process.env.DATABASE_URL || `postgresql://${dbUser}@127.0.0.1:5432/rawda_db`;

const pool = new Pool({ connectionString });

export const connectDatabase = async () => {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

      CREATE TABLE IF NOT EXISTS users (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          full_name VARCHAR(255) NOT NULL,
          email VARCHAR(255) UNIQUE NOT NULL,
          password VARCHAR(255) NOT NULL,
          role VARCHAR(50) DEFAULT 'student',
          created_at TIMESTAMP DEFAULT NOW()
      );

      CREATE TABLE IF NOT EXISTS students (
          id UUID PRIMARY KEY,
          user_id UUID REFERENCES users(id) ON DELETE CASCADE,
          student_code VARCHAR(100) UNIQUE NOT NULL,
          grade VARCHAR(100) DEFAULT 'عام',
          school VARCHAR(255) DEFAULT 'عام',
          created_at TIMESTAMP DEFAULT NOW()
      );
    `);
    console.log("🚀 [المدرس الذكي] تم تهيئة قاعدة البيانات والجداول من الصفر بنجاح!");
  } finally {
    client.release();
  }
};

export const getDatabasePool = () => pool;
