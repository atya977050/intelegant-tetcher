import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));


app.get('/api/health', (req, res) => { res.status(200).send('OK'); });

app.listen(PORT, () => {
  console.log(`🚀 [المعلم الذكي أونلاين] المنصة جاهزة تعمل على: http://localhost:${PORT}`);
});
