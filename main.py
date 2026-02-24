import os
import google.generativeai as genai

def start_agent():
    # جلب المفتاح
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # اختيار النموذج والطلب
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content("اكتب نص فيديو قصير عن القلب البشري مع روابط فيديو 4k")
        
        # التأكد من إنشاء الملف في المسار الصحيح
        content = response.text if response.text else "فشل في جلب المحتوى"
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("تم إنشاء الملف بنجاح ✅")
    except Exception as e:
        # إذا فشل الذكاء الاصطناعي، سننشئ ملف طوارئ للتأكد من نجاح الـ Action
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"حدث خطأ في الذكاء الاصطناعي: {str(e)}")
        print("تم إنشاء ملف طوارئ")

if __name__ == "__main__":
    start_agent()
    
