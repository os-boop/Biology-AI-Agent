import os
import google.generativeai as genai

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    # قائمة بكل المسميات المحتملة للموديلات لتجنب خطأ v1beta
    models_to_try = [
        'gemini-1.5-flash', 
        'gemini-1.0-pro', 
        'models/gemini-1.5-flash', 
        'models/gemini-pro'
    ]
    
    success = False
    last_error = ""

    for model_name in models_to_try:
        try:
            print(f"Trying model: {model_name}...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("اكتب خطة فيديو تعليمي عن القلب البشري بالعربي")
            
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print(f"Successfully connected with: {model_name} ✅")
            success = True
            break
        except Exception as e:
            last_error = str(e)
            continue

    if not success:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"فشل الاتصال بكل الموديلات. آخر خطأ: {last_error}")

if __name__ == "__main__":
    start_agent()
