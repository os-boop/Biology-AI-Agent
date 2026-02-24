import os
import google.generativeai as genai

def start_agent():
    # قراءة المفتاح من خزنة GitHub
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write("خطأ: لم يتم العثور على مفتاح GEMINI_API_KEY في إعدادات GitHub.")
        return

    genai.configure(api_key=api_key)
    
    try:
        # استخدام الموديل الأحدث والأكثر استقراراً
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("اكتب خطة فيديو تعليمي مفصلة عن القلب البشري بالعربي مع روابط فيديوهات")
        
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success! Plan generated. ✅")
        
    except Exception as e:
        error_msg = f"فشل الاتصال بجوجل. السبب التقني: {str(e)}"
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(error_msg)
        print(f"Error: {e}")

if __name__ == "__main__":
    start_agent()
