import os
import google.generativeai as genai

def start_agent():
    try:
        # 1. جلب المفتاح والتأكد منه
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("المفتاح غير موجود في الإعدادات!")
        
        # 2. إعداد الاتصال
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash') # نسخة أسرع وأحدث
        
        # 3. طلب المهمة
        prompt = "اكتب سيناريو فيديو قصير جداً عن وظيفة القلب البشري مع 3 روابط لفيديوهات من Pexels."
        response = model.generate_content(prompt)
        
        # 4. حفظ النتيجة
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success: File Created!")
        
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    start_agent()
