import streamlit as st
from backend import load_catalog, handle_user_input

st.title("GreenLife Foods Chatbot")
st.write("Interact with our chatbot to explore products and place orders!")

catalog = load_catalog()

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")
if st.button("Send"):
    bot_response = handle_user_input(user_input, catalog)
    st.session_state.history.append((user_input, bot_response))

for user_msg, bot_msg in st.session_state.history:
    st.write(f"**You:** {user_msg}")
    st.write(f"**Bot:** {bot_msg}")