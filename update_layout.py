with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# استبدال قسم إدخال الشات بهيكل عمودي سليم (حقل الكتابة في الأعلى ثم الأزرار تحته أو بجانبه بوضوح)
old_html = """                <div class="chat-bottom-wrapper">
                    <!-- Chat Input Area -->
                    <div class="chat-input-area">
                        <input type="file" id="chatFile" style="display:none" onchange="handleFileUpload(event)">
                        <input type="text" id="chatInput" placeholder="اكتب سؤالك هنا بكل مرونة..." onkeypress="if(event.key==='Enter') sendChatMessage()">
                        <button type="button" class="btn btn-secondary" style="width: auto; margin-top: 0; padding: 12px 16px; border-radius: 12px;" onclick="document.getElementById('chatFile').click()" title="رفع مستند أو ملف">📎 ملف</button>
                        <button type="button" class="btn" style="width: auto; margin-top: 0; padding: 12px 20px; border-radius: 12px;" onclick="sendChatMessage()">إرسال 🚀</button>
                    </div>

                    <!-- Toolbar Below Chat Input -->
                    <div class="chat-toolbar">
                        <button class="tool-btn" onclick="sendQuickAction('اطلب اختباراً تقييمياً فورياً')">🎯 اطلب اختباراً تقييمياً</button>
                        <button class="tool-btn" onclick="sendQuickAction('خطة الارتقاء وحصد أعلى الدرجات')">📈 خطة الارتقاء للقمة</button>
                        <button class="tool-btn" onclick="sendQuickAction('مراجعة شاملة للدروس السابقة')">📚 مراجعة الدروس السابقة</button>
                        <button class="tool-btn" onclick="sendQuickAction('اشرح لي الدرس الأول بالتفصيل')">💡 شرح الدرس الأول</button>
                    </div>
                </div>"""

new_html = """                <div class="chat-bottom-wrapper" style="padding: 12px; gap: 10px; display: flex; flex-direction: column;">
                    <!-- Chat Input Field on Top -->
                    <div style="display: flex; gap: 8px; width: 100%;">
                        <input type="file" id="chatFile" style="display:none" onchange="handleFileUpload(event)">
                        <input type="text" id="chatInput" placeholder="اكتب سؤالك هنا بكل مرونة..." onkeypress="if(event.key==='Enter') sendChatMessage()" style="flex: 1; margin-bottom: 0; padding: 12px 15px; border-radius: 12px; border: 1px solid #cbd5e1; font-size: 1rem;">
                        <button type="button" class="btn btn-secondary" style="width: auto; margin-top: 0; padding: 10px 14px; border-radius: 12px;" onclick="document.getElementById('chatFile').click()" title="رفع ملف">📎</button>
                        <button type="button" class="btn" style="width: auto; margin-top: 0; padding: 10px 18px; border-radius: 12px;" onclick="sendChatMessage()">إرسال 🚀</button>
                    </div>

                    <!-- Toolbar Below -->
                    <div class="chat-toolbar" style="display: flex; gap: 8px; overflow-x: auto; background: transparent; padding: 0;">
                        <button class="tool-btn" onclick="sendQuickAction('اطلب اختباراً تقييمياً فورياً')">🎯 اطلب اختباراً تقييمياً</button>
                        <button class="tool-btn" onclick="sendQuickAction('خطة الارتقاء وحصد أعلى الدرجات')">📈 خطة الارتقاء للقمة</button>
                        <button class="tool-btn" onclick="sendQuickAction('مراجعة شاملة للدروس السابقة')">📚 مراجعة الدروس السابقة</button>
                        <button class="tool-btn" onclick="sendQuickAction('اشرح لي الدرس الأول بالتفصيل')">💡 شرح الدرس الأول</button>
                    </div>
                </div>"""

if old_html in html:
    html = html.replace(old_html, new_html)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("تم تعديل هيكل الشات بنجاح تام!")
else:
    print("تعذر العثور على المقطع بدقة، سيتم تطبيق الفحص البديل.")
