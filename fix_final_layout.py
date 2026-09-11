with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# سنبحث عن منطقة الحاوية السفلية ونستبدلها بتصميم عمودي محكم 100%
new_bottom_wrapper = """                <div class="chat-bottom-wrapper" style="padding: 12px; background: #ffffff; border-top: 1px solid #e2e8f0; display: flex; flex-direction: column; gap: 10px;">
                    <!-- حقل الكتابة وزر الإرسال في الأعلى -->
                    <div style="display: flex; gap: 8px; width: 100%; align-items: center;">
                        <input type="file" id="chatFile" style="display:none" onchange="handleFileUpload(event)">
                        <input type="text" id="chatInput" placeholder="اكتب سؤالك هنا..." onkeypress="if(event.key==='Enter') sendChatMessage()" style="flex: 1; padding: 12px 15px; border-radius: 12px; border: 1px solid #cbd5e1; font-size: 1rem; outline: none;">
                        <button type="button" class="btn btn-secondary" style="padding: 12px 14px; border-radius: 12px; white-space: nowrap;" onclick="document.getElementById('chatFile').click()">📎</button>
                        <button type="button" class="btn" style="padding: 12px 18px; border-radius: 12px; white-space: nowrap;" onclick="sendChatMessage()">إرسال 🚀</button>
                    </div>

                    <!-- شريط الأزرار السريعة في الأسفل -->
                    <div class="chat-toolbar" style="display: flex; gap: 8px; overflow-x: auto; background: transparent; padding: 0; width: 100%;">
                        <button class="tool-btn" onclick="sendQuickAction('اطلب اختباراً تقييمياً فورياً')">🎯 اطلب اختباراً</button>
                        <button class="tool-btn" onclick="sendQuickAction('خطة الارتقاء وحصد أعلى الدرجات')">📈 خطة الارتقاء</button>
                        <button class="tool-btn" onclick="sendQuickAction('مراجعة شاملة للدروس السابقة')">📚 مراجعة الدروس</button>
                        <button class="tool-btn" onclick="sendQuickAction('اشرح لي الدرس الأول بالتفصيل')">💡 شرح الدرس</button>
                    </div>
                </div>"""

# استبدال الحاوية القديمة أياً كان محتواها الداخلي داخل السكشن الخاص بالدردشة
import re
# نبحث عن div يحمل الكلاس chat-bottom-wrapper
pattern = r'<div class="chat-bottom-wrapper".*?</div>\s*</div>\s*</div>'
# سنقوم بالاستبدال المباشر للقسم السفلي بالكامل بناءً على وسم البداية
start_idx = html.find('class="chat-bottom-wrapper"')
if start_idx != -1:
    # نرجع قليلاً للخلف لنبدأ من فتحة الـ div الحاضنة
    div_start = html.rfind('<div', 0, start_idx)
    # نبحث عن نهاية الـ div المناسبة (نستبدل الحاوية بأكملها)
    # للضمان، سنقوم بالبحث عن النص القديم أو استبداله بشكل دقيق
    print("تم العثور على مكان الحاوية، جاري التحديث...")

# طريقة أضمن: استبدال النص الحالي للـ chat-bottom-wrapper تماماً
old_block_marker = 'class="chat-bottom-wrapper"'
if old_block_marker in html:
    # سنقوم بكتابة سكربت يبحث عن عنصر الـ wrapper ويستبدله
    # لتجنب الأخطاء، سنقوم بتعديل ملف الـ html عبر كتابة قالب نظيف لمنطقة الدردشة السفلية
    pass

with open("public/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if 'class="chat-bottom-wrapper"' in line:
        skip = True
        new_lines.append(new_bottom_wrapper + "\n")
    elif skip:
        if '</div>' in line: # تخطي الأسطر القديمة التابعة للـ wrapper حتى إغلاقه
            skip = False
        continue
    else:
        new_lines.append(line)

with open("public/index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("تم ضبط وتعديل هيكل الشات بنجاح تام!")
