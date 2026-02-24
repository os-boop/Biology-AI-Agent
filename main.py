import os
import google.generativeai as genai

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # قائمة بأسماء الموديلات الممكنة لتجربتها آلياً
    models_to_try = ['gemini-1.5-flash', 'gemini-pro']
    
    content_generated = False
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("اكتب خطة فيديو تعليمي عن القلب البشري بالعربي مع روابط فيديوهات")
            
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Success with model: {model_name} ✅")
            content_generated = True
            break # توقف إذا نجح أحد الموديلات
        except Exception as e:
            print(f"Failed with {model_name}: {e}")

    if not content_generated:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write("لم نتمكن من الاتصال بالموديلات، يرجى التحقق من نسخة المكتبة.")

if __name__ == "__main__":
    start_agent()
