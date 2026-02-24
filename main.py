import os
import google.generativeai as genai
from google.generativeai.types import RequestOptions

def start_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    
    # الإعداد الأساسي
    genai.configure(api_key=api_key)

    # إجبار المكتبة على استخدام الإصدار المستقر v1 وتجربة الموديل الأكثر ضماناً
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # استخدام RequestOptions لإجبار النظام على تجاوز خطأ v1beta
        response = model.generate_content(
            "اكتب خطة فيديو تعليمي عن القلب البشري بالعربي",
            request_options=RequestOptions(api_version='v1')
        )
        
        with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success! Finally working. ✅")

    except Exception as e:
        # محاولة أخيرة بموديل برو مع نفس الإعدادات المستقرة
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(
                "اكتب خطة فيديو تعليمي عن القلب البشري بالعربي",
                request_options=RequestOptions(api_version='v1')
            )
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(response.text)
        except Exception as e2:
            with open("VIDEO_PLAN.md", "w", encoding="utf-8") as f:
                f.write(f"خطأ الإصدار النهائي: {str(e2)}")

if __name__ == "__main__":
    start_agent()
