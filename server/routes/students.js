import express from 'express';
import { getDatabasePool } from '../config/database.js';

const router = express.Router();

router.get('/', async (req, res) => {
  console.log('📥 طلب جلب قائمة الطلاب');
  try {
    const pool = getDatabasePool();
    const result = await pool.query(`
      SELECT u.id, u.full_name, u.email, u.created_at, s.student_code 
      FROM users u 
      LEFT JOIN students s ON u.id = s.user_id 
      WHERE u.role = 'student'
      ORDER BY u.created_at DESC
    `);
    
    return res.json({ students: result.rows });
  } catch (err) {
    console.error('🔥 خطأ أثناء جلب الطلاب:', err);
    return res.status(500).json({ error: 'خطأ في جلب بيانات الطلاب' });
  }
});

export default router;
