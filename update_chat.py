with open("public/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# استبدال تنسيق صندوق الإرسال والأزرار ليصبح عمودياً مرتباً
old_css = """.chat-bottom-wrapper { background: white; border-top: 1px solid #e2e8f0; display: flex; flex-direction: column; }
        .chat-input-area { display: flex; padding: 12px; gap: 10px; align-items: center; border-bottom: 1px solid #f1f5f9; }             .chat-input-area input[type="text"] { flex: 1; margin-bottom: 0; padding: 14px 18px; border-radius: 12px; font-size: 1rem; }
        .chat-toolbar { display: flex; padding: 10px 15px; gap: 8px; background: #f8fafc; overflow-x: auto; }"""

new_css = """.chat-bottom-wrapper { background: white; border-top: 1px solid #e2e8f0; display: flex; flex-direction: column; padding: 10px; gap: 8px; }
        .chat-input-area { display: flex; padding: 0; gap: 10px; align-items: center; width: 100%; order: 1; }
        .chat-input-area input[type="text"] { flex: 1; margin-bottom: 0; padding: 14px 18px; border-radius: 12px; font-size: 1rem; width: 100%; }
        .chat-toolbar { display: flex; padding: 4px 0; gap: 8px; background: transparent; overflow-x: auto; order: 2; width: 100%; }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("تم تحديث تنسيق الشات بنجاح!")
else:
    print("تأكد من مطابقة الإصدار، أو يمكنك تحديثه يدوياً.")
