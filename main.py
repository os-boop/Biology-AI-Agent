import google.generativeai as genai
import os

# الاتصال بمفتاحك السري المخزن في GitHub Secrets
genai.configure(api_key=os.environ["AIzaSyBZUgx5cBvJLIruuWtlUS0AWaR3lUMSpyQ"])

def start_agent():
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # الطلب الاحترافي للبحث عن فيديوهات 4K
    prompt = """
    Create a viral 50-second Biology script for YouTube Shorts (English).
    For each scene, give me a direct Pexels.com search link for 4K vertical videos.
    Provide the full Arabic translation for voice-over.
    """
    
    response = model.generate_content(prompt)
    
    # حفظ الخطة في ملف Markdown ليظهر لك على شكل صفحة جميلة
    with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
        f.write("# 🧬 Daily Biology Content Agent\n")
        f.write(response.text)

if __name__ == "__main__":
    start_agent()
