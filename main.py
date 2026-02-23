import google.generativeai as genai
import os

# جلب المفتاح من الخزنة
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def start_agent():
    model = genai.GenerativeModel('gemini-pro')
    # طلب خطة فيديو دقيقة
    prompt = "Create a 50-second Biology video plan about 'The Human Heart'. Provide 5 direct Pexels video links (vertical 4K) and Arabic script."
    
    response = model.generate_content(prompt)
    
    # حفظ النتيجة في ملف Markdown
    with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    start_agent()
