import os
import requests
import json

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    
    # سنستخدم هنا gemini-1.0-pro لأنه الأكثر توافقاً مع جميع الحسابات
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": "اكتب خطة فيديو تعليمي مفصلة عن القلب البشري بالعربي مع روابط فيديوهات"}]
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
            print("Done! Success at last. ✅")
        else:
            # إذا فشل، سنحاول مرة أخيرة بنسخة v1 لنفس الموديل
            url_v1 = url.replace("v1beta", "v1")
            response = requests.post(url_v1, headers=headers, data=json.dumps(payload))
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
            f.write(f"خطأ تقني: {str(e)}")

if __name__ == "__main__":
    start_agent()
