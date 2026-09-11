import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, "../public")));

app.get("/api/health", (req, res) => {
    res.status(200).json({ status: "ok" });
});

app.post("/api/chat", (req, res) => {
    const { message, action } = req.body;
    let reply = "أهلاً بك يا رفيق الدرب 🌿 أنا معك لمساعدتك في دروس الرياضيات والتمارين!";
    
    if (action === "test") {
        reply = "🎯 اختبار اليقين: كم عدد التفاحات إذا كان لديك 3 تفاحات وأخذت تفاحتان؟ (الإجابة: 1)";
    } else if (action === "plan") {
        reply = "📈 خطة الارتقاء: 1. مراجعة العد حتى 5. 2. التدرب على الجمع البسيط. 3. حل تمارين الأشكال الهندسية.";
    } else if (action === "explain") {
        reply = "💡 شرح الدرس الأول: التعرف على الأعداد من (0 إلى 5) وعد الأشياء بدقة يعني مطابقة كل عنصر برقم واحد بالتسلسل.";
    } else if (message) {
        if (message.includes("الجمع") || message.includes("جمع")) {
            reply = "الجمع التصاعدي هو إضافة عدد إلى آخر، مثل: 2 + 3 = 5. حاول حل هذا التمرين: 4 + 1 = كم؟";
        } else if (message.includes("مرحباً") || message.includes("السلام")) {
            reply = "وعليكم السلام ورحمة الله يا رفيق الدرب 🌿 كيف تشعر اليوم؟ هل نبدأ بحل التمارين؟";
        } else {
            reply = `سؤال جميل يا رفيق الدرب: "${message}". في الصف الأول الابتدائي، نتعلم كيف نفكر بهذه المسائل خطوة بخطوة!`;
        }
    }
    
    res.json({ reply });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
