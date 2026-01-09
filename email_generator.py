import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt_templates import email_prompt,improve_email_prompt

load_dotenv()

genai.configure(api_key=os.getenv("gemini_api_key"))

model=genai.GenerativeModel("gemini-2.5-flash")

def generate_email(purpose,tone,details,length="Medium",temperature=0.7):
    prompt=email_prompt(purpose,tone,details,length)
    try:
        response=model.generate_content(
            prompt,
            generation_config={
                "temperature":temperature
            }
        )
        return response.text
    except Exception as e:
        return f"⚠️Error generating email:{e}"
   

def improve_email(existing_email,tone="Professional",temperature=0.7):
    prompt=improve_email_prompt(existing_email,tone)

    try:
        response=model.generate_content(
            prompt,
             generation_config={
                "temperature":temperature
            }
        )
        return response.text
    except Exception as e:
        return f"⚠️Error improving email:{e}"