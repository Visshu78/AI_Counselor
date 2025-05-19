# app.py

import streamlit as st
from chatbot_engine import process_input

st.set_page_config(page_title="AI Counselor", layout="centered")
st.title("🧠 AI Counselor Chatbot")

# Session states
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ccbt_step" not in st.session_state:
    st.session_state.ccbt_step = 0
if "abc_step" not in st.session_state:
    st.session_state.abc_step = 0
if "using_abc" not in st.session_state:
    st.session_state.using_abc = False

# Chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot response
    bot_reply, st.session_state.ccbt_step, st.session_state.abc_step, st.session_state.using_abc = process_input(
        user_input,
        st.session_state.ccbt_step,
        st.session_state.abc_step,
        st.session_state.using_abc
    )

    # Display bot message
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
