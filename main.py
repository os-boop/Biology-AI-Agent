import os
import requests
import json

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    
    # الرابط السحري: استخدام v1beta مع الموديل بدون أرقام فرعية معقدة
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": "اكتب خطة فيديو تعليمي مفصلة عن القلب البشري بالعربي"}]
        }]
    }
    
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        
        # إذا نجح الاتصال
        if 'candidates' in result:
            text_content = result['candidates'][0]['content']['parts'][0]['text']
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(text_content)
            print("نجاح باهر! الخطة جاهزة. ✅")
        else:
            # محاولة أخيرة بموديل gemini-pro إذا فشل flash
            url_pro = url.replace("gemini-1.5-flash", "gemini-pro")
            response = requests.post(url_pro, headers=headers, data=json.dumps(payload))
            result = response.json()
            
            if 'candidates' in result:
                text_content = result['candidates'][0]['content']['parts'][0]['text']
                with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                    f.write(text_content)
            else:
                # كتابة الخطأ بوضوح لنعرف ما يطلبه جوجل بالضبط
                with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                    f.write(f"رد جوجل الأخير: {json.dumps(result, ensure_ascii=False)}")
                
    except Exception as e:
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(f"خطأ في الطلب المباشر: {str(e)}")

if __name__ == "__main__":
    start_agent()
