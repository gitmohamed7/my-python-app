from groq import Groq
from config import API_KEY

client = Groq(api_key=API_KEY)

def chat(user_message):
    message = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": user_message}]
    )
    return message.choices[0].message.content