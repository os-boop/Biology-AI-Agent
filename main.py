import os
import requests
import json

def start_agent():
    # 1. جلب المفتاح من الخزنة
    api_key = os.getenv("GEMINI_API_KEY")
    
    # 2. الرابط المباشر لجوجل (الإصدار المستقر v1)
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # 3. محتوى الطلب
    payload = {
        "contents": [{
            "parts": [{"text": "اكتب خطة فيديو تعليمي مفصلة عن القلب البشري بالعربي مع روابط فيديوهات"}]
        }]
    }
    
    headers = {'Content-Type': 'application/json'}

    try:
        # 4. إرسال الطلب يدوياً وتجاوز المكتبة المتعطلة
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        
        # 5. استخراج النص وحفظه
        if 'candidates' in result:
            text_content = result['candidates'][0]['content']['parts'][0]['text']
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(text_content)
            print("Success! Finally bypass completed. ✅")
        else:
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(f"خطأ من جوجل: {json.dumps(result, ensure_ascii=False)}")
                
    except Exception as e:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"فشل الاتصال المباشر: {str(e)}")

if __name__ == "__main__":
    start_agent()
