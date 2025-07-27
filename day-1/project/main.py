from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Tell me a dark joke in Bahasa Indonesia, but make sure it's not offensive. The joke is about politics."},
    ]
)

print(response.choices[0].message.content)
