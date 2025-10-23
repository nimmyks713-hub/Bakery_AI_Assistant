# 🎂 Home Bakery AI Assistant

Welcome to **Nims World Cakes 🍰**, an AI-powered bakery assistant built with **Streamlit** and **Google Gemini API**.  
This interactive chatbot helps customers browse the menu, place cake orders, and receive cheerful order summaries — all powered by generative AI! 🧁

🌐 **Live Demo:** [Try it on Streamlit Cloud](https://homebakeryai.streamlit.app/)  

---

## ✨ Features

- 💬 **Interactive Chatbot:** Friendly AI assistant that guides customers step-by-step through the order process.  
- 🎂 **Dynamic Cake Menu:** Loads menu details from `menu.json` and displays them clearly.  
- 📍 **Location + Delivery Time:** Collects delivery details conversationally.  
- 🎉 **Order Summary:** Generates a personalized, emoji-filled summary with all order details.  
- 🔒 **Secure API Integration:** Uses `.env` for Google Gemini API keys.  
- ☁️ **Deployed on Streamlit Cloud** for instant online access.

---

## 🛠️ Tech Stack

| Component | Description |
|------------|-------------|
| **Frontend** | Streamlit |
| **AI Engine** | Google Gemini (via `google-generativeai`) |
| **Backend Logic** | Python |
| **Environment Management** | `python-dotenv` |
| **Data Source** | `menu.json` |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/nimmyks713-hub/Bakery_AI_Assistant.git
cd Bakery_AI_Assistant
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
###4️⃣ Add Your API Key
Create a .env file and add:
```
LLM_API_KEY=your_google_gemini_api_key_here
```
###5️⃣ Run the App
```bash
streamlit run app.py
```
---
## ☁️ Deployment

The app is hosted on Streamlit Cloud.
To deploy:

-Push your code to GitHub.

-Connect your repo to Streamlit Cloud.

-Set environment variable LLM_API_KEY in the app settings.

-Click Deploy 🚀

