from openai import OpenAI
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_ai(user_mesage):
  """Simple function to chat with AI."""
  try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and friendly AI assistant."},
            {"role": "user", "content": user_mesage}
        ],
        temperature=0.7, # Adjust temperature for creativity
    )
    return response.choices[0].message.content
  except Exception as e:
    return f"Error: {str(e)}"
  
def main():
  print("🤖 Welcome to your first AI application!")
  print("Type 'quit' to exit\n")

  while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
      print("👋 Goodbye!")
      break
    
    response = chat_with_ai(user_input)
    print(f"AI: {response}")

if __name__ == "__main__":
  main()
  print(f"Session ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")