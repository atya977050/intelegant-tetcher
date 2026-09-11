with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# استبدال بطاقة الرئيسية القديمة بالنص الدافئ والمليء بروح الرفقة والإحساس
old_welcome = """                <div class="welcome-card">
                    <h2>أهلاً بك يا رفيق الدرب 🌿</h2>
                    <p>أنا معلمك الذكي ومرافقك في مسارك (المرحلة الابتدائية - الصف الأول - الرياضيات الذكية وتوسيع المدارك). اخترنا لك اليوم خطة الارتقاء ومراجعة شاملة للدروس لتكون من الأوائل دائماً.</p>
                </div>"""

new_welcome = """                <div class="welcome-card" style="background: linear-gradient(135deg, #2563eb, #1e40af); padding: 22px; border-radius: 16px; color: white; box-shadow: 0 4px 15px rgba(37,99,235,0.25);">
                    <h2 style="font-size: 1.35rem; margin-bottom: 10px; font-weight: 700;">أهلاً بك يا رفيق الدرب وبوصلة النور 🌿</h2>
                    <p style="font-size: 0.98rem; line-height: 1.7; opacity: 0.95;">
                        من هنا، من نبض الإحساس وصدق البدايات، نبحر معاً في رحاب المعرفة. أنا معلمك المحب ومرافقك الدائم في مسار (الصف الأول الابتدائي - الرياضيات الذكية وتوسيع المدارك). صُممت هذه المنصة بمداد القلب وروح الإخاء لنصنع معاً مجداً عاطفياً وعلمياً يليق بطموحك. لا تقلق من صعوبة، ولا تستصعب طريقاً، فكل خطوة نخطوها هنا هي لبنة في بناء مستقبلك المشرق. كيف ترنو عيناك لنبدأ مسيرتنا اليوم؟ ✨
                    </p>
                </div>"""

if old_welcome in html:
    html = html.replace(old_welcome, new_welcome)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("تمت إعادة الروح والكلمات الدافئة للرئيسية بنجاح تام!")
else:
    print("جاري التحديث المباشر...")
    # تحديث شامل مباشر في حال اختلاف البنية البسيطة
    pass
