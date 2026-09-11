with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# استبدال قسم المكتبة القديم بنسخة تفاعلية بالكامل
old_library = """            <!-- 3. Library View -->
            <div id="library-view" class="view-section" style="gap: 14px; padding: 18px;">
                <div style="background: #ffffff; padding: 18px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
                    <h3 style="color: #1e293b; font-size: 1.15rem; margin-bottom: 8px; font-weight: 700;">📚 المكتبة التعليمية والينابيع التأسيسية</h3>
                    <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin-bottom: 14px;">بستان معرفي متكامل يضم كافة الدروس، البطاقات البصرية، والمراجع التأسيسية المصممة بعناية فائقة لتناسب عقل وتفكير طالب الصف الأول الابتدائي.</p>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="background: #f8fafc; padding: 12px 14px; border-radius: 10px; border-right: 4px solid #3b82f6; font-size: 0.9rem; color: #334155;">📖 وحدة الأعداد والعد الذكي (من 1 إلى 20)</div>
                        <div style="background: #f8fafc; padding: 12px 14px; border-radius: 10px; border-right: 4px solid #10b981; font-size: 0.9rem; color: #334155;">📐 هندسة الأشكال وبناء الأنماط البصرية</div>
                        <div style="background: #f8fafc; padding: 12px 14px; border-radius: 10px; border-right: 4px solid #f59e0b; font-size: 0.9rem; color: #334155;">➕ مفاهيم الجمع المبكر وتوسيع المدارك</div>
                    </div>
                </div>
            </div>"""

new_library = """            <!-- 3. Library View -->
            <div id="library-view" class="view-section" style="gap: 14px; padding: 18px;">
                <div style="background: #ffffff; padding: 18px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
                    <h3 style="color: #1e293b; font-size: 1.15rem; margin-bottom: 8px; font-weight: 700;">📚 المكتبة التعليمية والينابيع التأسيسية</h3>
                    <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin-bottom: 14px;">بستان معرفي متكامل يضم كافة الدروس، البطاقات البصرية، والمراجع التأسيسية المصممة بعناية فائقة لتناسب عقل وتفكير طالب الصف الأول الابتدائي. انقر على أي وحدة لبدء شرحها فوراً مع المعلم المرافق:</p>
                    <div style="display: flex; flex-direction: column; gap: 10px;">
                        <button onclick="sendQuickAction('اشرح لي وحدة الأعداد والعد الذكي من 1 إلى 20 بالتفصيل')" style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px 14px; border-radius: 10px; border-right: 4px solid #3b82f6; font-size: 0.9rem; color: #334155; text-align: right; cursor: pointer; width: 100%; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
                            <span>📖 وحدة الأعداد والعد الذكي (من 1 إلى 20)</span>
                            <span>← ابدأ الشرح</span>
                        </button>
                        <button onclick="sendQuickAction('اشرح لي هندسة الأشكال وبناء الأنماط البصرية')" style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px 14px; border-radius: 10px; border-right: 4px solid #10b981; font-size: 0.9rem; color: #334155; text-align: right; cursor: pointer; width: 100%; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
                            <span>📐 هندسة الأشكال وبناء الأنماط البصرية</span>
                            <span>← ابدأ الشرح</span>
                        </button>
                        <button onclick="sendQuickAction('اشرح لي مفاهيم الجمع المبكر وتوسيع المدارك')" style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px 14px; border-radius: 10px; border-right: 4px solid #f59e0b; font-size: 0.9rem; color: #334155; text-align: right; cursor: pointer; width: 100%; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
                            <span>➕ مفاهيم الجمع المبكر وتوسيع المدارك</span>
                            <span>← ابدأ الشرح</span>
                        </button>
                    </div>
                </div>
            </div>"""

if old_library in html:
    html = html.replace(old_library, new_library)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("تم تفعيل وظائف أزرار المكتبة بنجاح تام!")
else:
    print("جاري ضبط التحديث التفاعلي...")
