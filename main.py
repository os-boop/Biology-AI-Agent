import os
import requests
import json

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    
    # هذا الرابط هو "المفتاح السحري" الذي يتوافق مع حسابات جوجل الجديدة
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": "اكتب خطة فيديو تعليمي عن القلب البشري بالعربي بالتفصيل"}]
        }]
    }
    
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        
        if 'candidates' in result:
            text_content = result['candidates'][0]['content']['parts'][0]['text']
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(text_content)
            print("Success! The wall is broken. ✅")
        else:
            # إذا استمر العناد، سنكتب الرد الكامل لنفهمه
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(f"رد جوجل التفصيلي: {json.dumps(result, ensure_ascii=False)}")
                
    except Exception as e:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"خطأ غير متوقع: {str(e)}")

if __name__ == "__main__":
    start_agent()
