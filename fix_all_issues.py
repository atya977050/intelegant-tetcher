import os

# التأكد من وجود مجلد public
os.makedirs("public", exist_ok=True)

# 1. تحديث server.cjs لضمان توجيه الصفحة الرئيسية بشكل صحيح وسلس
server_code = """const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));

app.listen(PORT, () => {
    console.log(`منصة المعلم الذكي أونلاين تعمل الآن بسلام على الرابط: http://localhost:${PORT}`);
});
"""

with open("server.cjs", "w", encoding="utf-8") as f:
    f.write(server_code)

# 2. تحديث index.html بحيث يبدأ بـ (الرئيسية) أو يعرض الأقسام بمرونة مع شات مرتب عمودياً تماماً
html_code = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة المعلم الذكي أونلاين</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background: #f8fafc; color: #1e293b; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }
        
        /* App Container */
        .app-container { display: flex; flex-direction: column; height: 100%; width: 100%; max-width: 600px; margin: 0 auto; background: #ffffff; box-shadow: 0 0 15px rgba(0,0,0,0.05); }

        /* Top Navigation / Header */
        .app-header { background: #1e293b; color: white; padding: 12px 15px; display: flex; flex-direction: column; gap: 8px; }
        .nav-tabs { display: flex; gap: 6px; overflow-x: auto; scrollbar-width: none; padding-bottom: 2px; }
        .nav-tabs::-webkit-scrollbar { display: none; }
        .nav-tab { background: rgba(255,255,255,0.1); border: none; color: #cbd5e1; padding: 6px 12px; border-radius: 6px; font-size: 0.85rem; cursor: pointer; white-space: nowrap; }
        .nav-tab.active { background: #3b82f6; color: white; font-weight: 600; }

        /* Content Area */
        .content-area { flex: 1; overflow-y: auto; background: #fdfdfd; display: flex; flex-direction: column; }
        
        /* Views */
        .view-section { display: none; padding: 15px; flex-direction: column; gap: 12px; height: 100%; }
        .view-section.active { display: flex; }

        /* Home View Styles */
        .welcome-card { background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2); }
        .welcome-card h2 { font-size: 1.25rem; margin-bottom: 8px; }
        .welcome-card p { font-size: 0.95rem; line-height: 1.5; opacity: 0.95; }

        /* Chat View Styles */
        .chat-messages { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; padding-bottom: 10px; }
        .message { padding: 10px 14px; border-radius: 12px; max-width: 88%; line-height: 1.5; font-size: 0.9rem; }
        .message.bot { background: #f1f5f9; color: #334155; align-self: flex-start; border-bottom-right-radius: 4px; }
        .message.user { background: #3b82f6; color: white; align-self: flex-end; border-bottom-left-radius: 4px; }

        /* Bottom Fixed Wrapper for Chat */
        .chat-bottom-wrapper { background: #ffffff; border-top: 1px solid #e2e8f0; padding: 10px 12px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0; }
        
        /* Input Row: Strictly stacked & separated */
        .chat-input-row { display: flex; gap: 6px; width: 100%; align-items: center; }
        .chat-input-row input[type="text"] { flex: 1; padding: 10px 12px; border-radius: 10px; border: 1px solid #cbd5e1; font-size: 0.9rem; outline: none; background: #fff; }
        
        .action-btn { background: #3b82f6; color: white; border: none; padding: 10px 14px; border-radius: 10px; font-weight: 600; cursor: pointer; white-space: nowrap; font-size: 0.85rem; }
        .file-btn { background: #e2e8f0; color: #334155; border: none; padding: 10px 12px; border-radius: 10px; cursor: pointer; white-space: nowrap; font-size: 0.85rem; }

        /* Toolbar Row Below Input */
        .chat-toolbar { display: flex; gap: 6px; overflow-x: auto; width: 100%; scrollbar-width: none; }
        .chat-toolbar::-webkit-scrollbar { display: none; }
        .tool-btn { flex: 0 0 auto; background: #f8fafc; border: 1px solid #e2e8f0; color: #475569; padding: 6px 10px; border-radius: 6px; font-size: 0.78rem; cursor: pointer; white-space: nowrap; }
    </style>
</head>
<body>

    <div class="app-container">
        <!-- Header & Navigation Tabs -->
        <header class="app-header">
            <h1 style="font-size: 1.1rem;">منصة المعلم الذكي أونلاين 🌿</h1>
            <nav class="nav-tabs">
                <button class="nav-tab active" onclick="switchView('home', this)">🏠 الرئيسية</button>
                <button class="nav-tab" onclick="switchView('chat', this)">🤖 الشات والمساعد</button>
                <button class="nav-tab" onclick="switchView('library', this)">📚 المكتبة</button>
                <button class="nav-tab" onclick="switchView('tests', this)">✍️ اختبارات اليقين</button>
                <button class="nav-tab" onclick="switchView('companions', this)">🤝 رفقة الدرب</button>
            </nav>
        </header>

        <!-- Main Content Area -->
        <div class="content-area">
            
            <!-- 1. Home View -->
            <div id="home-view" class="view-section active">
                <div class="welcome-card">
                    <h2>أهلاً بك يا رفيق الدرب 🌿</h2>
                    <p>أنا معلمك الذكي ومرافقك في مسارك (المرحلة الابتدائية - الصف الأول - الرياضيات الذكية وتوسيع المدارك). اخترنا لك اليوم خطة الارتقاء ومراجعة شاملة للدروس لتكون من الأوائل دائماً.</p>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 5px;">
                    <button class="action-btn" style="width: 100%; text-align: right; padding: 12px;" onclick="switchView('chat', document.querySelector('.nav-tab:nth-child(2)'))">🤖 ابدأ الشات مع المعلم المرافق</button>
                    <button class="file-btn" style="width: 100%; text-align: right; padding: 12px; background: #f1f5f9;" onclick="switchView('tests', document.querySelector('.nav-tab:nth-child(4)'))">🎯 اطلب اختباراً تقييمياً فورياً</button>
                </div>
            </div>

            <!-- 2. Chat View -->
            <div id="chat-view" class="view-section" style="padding: 10px; justify-content: space-between;">
                <div class="chat-messages" id="chatMessages">
                    <div class="message bot">
                        أهلاً بك يا رفيق الدرب 🌿 أنا معلمك الذكي ومرافقك في مسارك (الصف الأول - الرياضيات الذكية). كيف أساعدك اليوم لتكون من الأوائل؟
                    </div>
                </div>

                <!-- Bottom Wrapper: Strictly Columnar Layout -->
                <div class="chat-bottom-wrapper">
                    <div class="chat-input-row">
                        <input type="file" id="chatFile" style="display:none" onchange="handleFileUpload(event)">
                        <input type="text" id="chatInput" placeholder="اكتب سؤالك هنا..." onkeypress="if(event.key==='Enter') sendChatMessage()">
                        <button type="button" class="file-btn" onclick="document.getElementById('chatFile').click()" title="رفع ملف">📎 ملف</button>
                        <button type="button" class="action-btn" onclick="sendChatMessage()">إرسال 🚀</button>
                    </div>

                    <div class="chat-toolbar">
                        <button class="tool-btn" onclick="sendQuickAction('اطلب اختباراً تقييمياً فورياً')">🎯 اختبار تقييمي</button>
                        <button class="tool-btn" onclick="sendQuickAction('خطة الارتقاء وحصد أعلى الدرجات')">📈 خطة الارتقاء</button>
                        <button class="tool-btn" onclick="sendQuickAction('مراجعة شاملة للدروس السابقة')">📚 مراجعة الدروس</button>
                        <button class="tool-btn" onclick="sendQuickAction('اشرح لي الدرس الأول بالتفصيل')">💡 شرح الدرس الأول</button>
                    </div>
                </div>
            </div>

            <!-- 3. Library View -->
            <div id="library-view" class="view-section">
                <h3 style="color: #334155; font-size: 1rem;">📚 المكتبة التعليمية</h3>
                <p style="font-size: 0.9rem; color: #64748b;">جميع الدروس والمراجع التأسيسية للصف الأول الابتدائي متوفرة هنا.</p>
            </div>

            <!-- 4. Tests View -->
            <div id="tests-view" class="view-section">
                <h3 style="color: #334155; font-size: 1rem;">✍️ اختبارات اليقين القصيرة</h3>
                <p style="font-size: 0.9rem; color: #64748b;">سؤال: كيف نضمن بناء تفكير رياضي ومنطقي سليم بدون أخطاء؟</p>
            </div>

            <!-- 5. Companions View -->
            <div id="companions-view" class="view-section">
                <h3 style="color: #334155; font-size: 1rem;">🤝 رفقة الدرب</h3>
                <p style="font-size: 0.9rem; color: #64748b;">هنا نلتقي لنرتقي معاً نحو قمم التفوق الدراسي.</p>
            </div>

        </div>
    </div>

    <script>
        function switchView(viewName, tabElement) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-tab').forEach(el => el.classList.remove('active'));
            
            document.getElementById(viewName + '-view').classList.add('active');
            if(tabElement) tabElement.classList.add('active');
        }

        function sendChatMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if(!text) return;
            
            const messagesContainer = document.getElementById('chatMessages');
            
            const userMsg = document.createElement('div');
            userMsg.className = 'message user';
            userMsg.textContent = text;
            messagesContainer.appendChild(userMsg);
            
            input.value = '';
            messagesContainer.scrollTop = messagesContainer.scrollHeight;

            // رد تلقائي ذكي من المعلم المرافق
            setTimeout(() => {
                const botMsg = document.createElement('div');
                botMsg.className = 'message bot';
                botMsg.textContent = "أحسنت يا رفيق الدرب 🌿 لقد استلمت سؤالك وجاري تحليل الإجابة لنصل معاً إلى القمة!";
                messagesContainer.appendChild(botMsg);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }, 600);
        }

        function sendQuickAction(actionText) {
            switchView('chat', document.querySelector('.nav-tab:nth-child(2)'));
            document.getElementById('chatInput').value = actionText;
            sendChatMessage();
        }

        function handleFileUpload(event) {
            const file = event.target.files[0];
            if(file) {
                switchView('chat', document.querySelector('.nav-tab:nth-child(2)'));
                const messagesContainer = document.getElementById('chatMessages');
                const fileMsg = document.createElement('div');
                fileMsg.className = 'message user';
                fileMsg.textContent = `📎 تم إرفاق الملف: ${file.name}`;
                messagesContainer.appendChild(fileMsg);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }
        }
    </script>
</body>
</html>
"""

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("تم ضبط وتحديث كافة إعدادات المنصة والهيكل بنجاح تام!")
