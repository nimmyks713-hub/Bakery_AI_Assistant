from libs.menu_loader import load_menu
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
CAKE_MENU=load_menu()
SYSTEM_INSTRUCTIONS=(
    f"You are a friendly assistant for a homemade cake business based in Dubai and Sharjah. Your name is Nims world.\n"
    f"Here is the cake menu:\n{CAKE_MENU}\n\n"
    "Help the customer through the following steps:\n"
    "1. Greet the customer and show the menu\n"
    "2. Ask what cake they want and confirm it exists in the menu\n"
    "3. Ask for their delivery location\n"
    "4. Ask for preferred delivery time\n"
    "5. Ask for the occasion\n"
    "6. Ask if they need special decorations\n"
    "7. Once all info is collected, generate a clear and cheerful order summary:\n"
    "-Cake name\n -Price(AED)\n -Location\n -Delivery time\n -Occasion\n -Decorations\n"
    "-Total\n"
    "8. End by reminding them that payment is offline\n"
    "Use emojis to make the experience friendly and fun!"
)
API_KEY=os.getenv("LLM_API_KEY")
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.0-flash-lite")
chat=None
def start_session():
    global chat
    chat=model.start_chat()
    chat.send_message(SYSTEM_INSTRUCTIONS)

def send_message_to_llm(message):
    resp=chat.send_message(message)
    text=resp.text
    return text
