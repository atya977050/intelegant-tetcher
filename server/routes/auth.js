import express from 'express';
import crypto from 'crypto';
import jwt from 'jsonwebtoken';
import { getDatabasePool } from '../config/database.js';

const router = express.Router();
const JWT_SECRET = process.env.JWT_SECRET || 'smart_teacher_secret_key_2026';

function hashPassword(password) {
  const salt = crypto.randomBytes(16).toString('hex');
  const hash = crypto.scryptSync(password, salt, 64).toString('hex');
  return `${salt}:${hash}`;
}

function verifyPassword(password, storedHash) {
  const [salt, key] = storedHash.split(':');
  const hash = crypto.scryptSync(password, salt, 64).toString('hex');
  return crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(key, 'hex'));
}

router.post('/register', async (req, res) => {
  try {
    const { fullName, email, password } = req.body;
    
    if (!fullName || !email || !password) {
      return res.status(400).json({ error: 'جميع الحقول مطلوبة' });
    }

    const pool = getDatabasePool();
    
    const existingUser = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (existingUser.rows.length > 0) {
      return res.status(400).json({ error: 'البريد الإلكتروني مستخدم بالفعل' });
    }

    const hashedPassword = hashPassword(password);
    
    const userResult = await pool.query(
      `INSERT INTO users (full_name, email, password_hash, role) VALUES ($1, $2, $3, 'student') RETURNING id, full_name, email, role`,
      [fullName, email, hashedPassword]
    );

    const newUser = userResult.rows[0];
    const studentCode = 'STU-' + Math.floor(100000 + Math.random() * 900000);

    await pool.query(
      `INSERT INTO students (user_id, student_code) VALUES ($1, $2)`,
      [newUser.id, studentCode]
    );

    const token = jwt.sign({ id: newUser.id, email: newUser.email, role: newUser.role }, JWT_SECRET, { expiresIn: '7d' });

    return res.status(201).json({
      message: 'تم إنشاء الحساب بنجاح',
      token,
      user: { id: newUser.id, full_name: newUser.full_name, email: newUser.email, role: newUser.role }
    });
  } catch (err) {
    console.error('🔥 خطأ في التسجيل:', err);
    return res.status(500).json({ error: 'خطأ داخلي في الخادم أثناء التسجيل' });
  }
});

router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ error: 'البريد وكلمة المرور مطلوبان' });
    }

    const pool = getDatabasePool();
    const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);

    if (result.rows.length === 0) {
      return res.status(400).json({ error: 'البريد الإلكتروني أو كلمة المرور غير صحيحة' });
    }

    const user = result.rows[0];
    const isMatch = verifyPassword(password, user.password_hash);

    if (!isMatch) {
      return res.status(400).json({ error: 'البريد الإلكتروني أو كلمة المرور غير صحيحة' });
    }

    const token = jwt.sign({ id: user.id, email: user.email, role: user.role }, JWT_SECRET, { expiresIn: '7d' });

    return res.json({
      message: 'تم تسجيل الدخول بنجاح',
      token,
      user: { id: user.id, full_name: user.full_name, email: user.email, role: user.role }
    });
  } catch (err) {
    console.error('🔥 خطأ في تسجيل الدخول:', err);
    return res.status(500).json({ error: 'خطأ داخلي في الخادم أثناء تسجيل الدخول' });
  }
});

export default router;
