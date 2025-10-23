import streamlit as st
from libs.menu_loader import load_menu
from libs.llm_test import start_session,send_message_to_llm
CAKE_MENU=load_menu()
st.title("🎂Home Bakery AI Assistant🎂")
st.markdown("Serving Dubai and Sharjah| Homemade Cakes🎂| Payment on delivery")

user_input=st.chat_input("Enter your message...")
if "messages" not in st.session_state:
    start_session()
    welcome_message=(
        "Hi there! Welcome to Nims world cakes\n\n"
        "Here's our menu:\n" + CAKE_MENU + "\n\n"
        "Would you like to order?"
    )
    st.session_state.messages=[{
        "role":"ai",
        "content":welcome_message
    }]

if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })
    llm_resp=send_message_to_llm(user_input)
    st.session_state.messages.append({
        "role":"ai",
        "content":llm_resp
    })

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


