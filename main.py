import os
import requests
import json

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    
    # استخدام المسمى الأحدث 'gemini-1.5-flash-latest' مع الإصدار المستقر v1
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": "اكتب خطة فيديو تعليمي مفصلة عن القلب البشري بالعربي"}]
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
            print("Done! The plan is ready. ✅")
        else:
            # إذا استمر الخطأ، سنقوم بتجربة 'gemini-1.5-flash' بدون كلمة latest
            url_alt = url.replace("-latest", "")
            response = requests.post(url_alt, headers=headers, data=json.dumps(payload))
            result = response.json()
            
            if 'candidates' in result:
                text_content = result['candidates'][0]['content']['parts'][0]['text']
                with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                    f.write(text_content)
            else:
                with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                    f.write(f"رد جوجل النهائي: {json.dumps(result, ensure_ascii=False)}")
                
    except Exception as e:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"خطأ في الاتصال: {str(e)}")

if __name__ == "__main__":
    start_agent()
            
