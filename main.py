import os
import google.generativeai as genai

def start_agent():
    # 1. جلب المفتاح
    api_key = os.getenv("GEMINI_API_KEY")
    
    # 2. إعداد بسيط جداً
    genai.configure(api_key=api_key)

    try:
        # 3. محاولة مباشرة بدون أي تعقيدات إضافية
        # استخدمنا اسم الموديل بدون أي مسارات (models/) لتجنب خطأ 404
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("اكتب خطة فيديو تعليمي عن القلب البشري بالعربي")
        
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success! ✅")

    except Exception as e:
        # محاولة أخيرة بموديل gemini-pro إذا فشل الفلاش
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("اكتب خطة فيديو تعليمي عن القلب البشري بالعربي")
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(response.text)
        except Exception as e2:
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(f"خطأ الاتصال الأخير: {str(e2)}")

if __name__ == "__main__":
    start_agent()
