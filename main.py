import os
import google.generativeai as genai

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write("API KEY غير موجودة في الإعدادات ❌")
        return

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("اكتب خطة فيديو قصيرة عن التنفس الخلوي")
        
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("نجاح ✅")
        
    except Exception as e:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"حدث خطأ أثناء الاتصال: {str(e)}")
        print(f"فشل: {e}")

if __name__ == "__main__":
    start_agent()
