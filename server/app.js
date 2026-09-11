
const express = require("express");
const path = require("path");
const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "../public")));

// مسار فحص الصحة المطلوب من Railway
app.get("/api/health", (req, res) => {
  res.status(200).send("OK");
});

// مسار المنصات والروابط الخارجية
app.get("/api/platforms", (req, res) => {
  res.json({
    platforms: [
      { name: "منصة الدروس الذكية", url: "#", desc: "شروحات مبسطة لمناهج الصف الأول الابتدائي" },
      { name: "بنك اختبارات اليقين", url: "#", desc: "تمارين وأسئلة تفاعلية لقياس الفهم" },
      { name: "مكتبة رفقة الدرب", url: "#", desc: "قصص ومراجع رياضيات ممتعة" }
    ]
  });
});

// مسار الشات والتفاعل الذكي مع الأدوات
app.post("/api/chat", (req, res) => {
  const { message, action } = req.body;
  let reply = "أهلاً بك يا رفيق الدرب 🌿 لقد استلمت طلبك وجاري العمل عليه لتكون من الأوائل دائماً!";

  if (action === "test") {
    reply = "🎯 **اختبار اليقين:** احسب الناتج التالي: مع مريم 5 تفاحات أكلت منها 2، فكم تفاحة بقيت معها؟";
  } else if (action === "plan") {
    reply = "📈 **خطة الارتقاء:** 1. مراجعة الأعداد من 1 إلى 10 اليوم. 2. حل 3 تمارين جمع بسيطة. 3. أخذ استراحة قصيرة.";
  } else if (action === "lessons") {
    reply = "📚 **مراجعة الدروس:** درسنا اليوم يدور حول الجمع التصاعدي بطريقة ممتعة وسريعة باستخدام الأصابع!";
  } else if (message) {
    reply = `🌿 استلمت سؤالك: "${message}". الإجابة النموذجية: ممتاز يا بطل، واصل التدريب فالتفوق حليفك!`;
  }

  res.json({ reply });
});

// رفع الملفات
app.post("/api/upload", (req, res) => {
  res.json({ success: true, message: "📎 تم استلام الملف وتحليله بنجاح يا رفيق الدرب!" });
});

app.listen(PORT, () => {
  console.log(`🚀 [المعلم الذكي أونلاين] المنصة جاهزة تعمل على: http://localhost:${PORT}`);
});
