import os
import google.generativeai as genai

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    # إعداد المكتبة لاستخدام النسخة المستقرة
    genai.configure(api_key=api_key)

    try:
        # جرب الموديل المستقر "gemini-1.5-flash" بدون بادئة الإصدار
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("اكتب خطة فيديو تعليمي عن القلب البشري بالعربي")
        
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success: Plan Generated! ✅")
        
    except Exception as e:
        # إذا فشل الفلاش، جرب البرو كخطة احتياطية فورية
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("اكتب خطة فيديو تعليمي عن القلب البشري بالعربي")
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(response.text)
        except Exception as e2:
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(f"فشل الاتصال النهائي. السبب: {str(e2)}")
