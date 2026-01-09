def email_prompt(purpose,tone,details,length="Medium"):
    return f"""
You are a professional email writer.
write an email with the following details:
Purpose:{purpose}
Tone:{tone}
Additional details:{details}

Rules:
- Use proper subject line
- Use professional formatting
- Be clear and concise
"""

def improve_email_prompt(existing_email,tone="Professinal"):
    return f"""
You are a professional email editor.
Improve the following email for clarity , tone and professionism.Keep meaning intact.
Tone:{tone}

Original email:
{existing_email}
"""