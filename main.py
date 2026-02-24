import os
import google.generativeai as genai

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

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
            break 
        except Exception as e:
            print(f"Failed with model {model_name}: {e}")

    if not content_generated:
        error_msg = "فشل الاتصال بالموديلات. يرجى التحقق من مفتاح الـ API وصلاحيته."
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(error_msg)

if __name__ == "__main__":
    start_agent()
