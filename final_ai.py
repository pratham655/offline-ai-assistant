import streamlit as st
import ollama

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Offline AI Chatbot", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #1e293b);
    color: white;
}
h1 {
    text-align: center;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Offline AI Chatbot")

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ---------------- INPUT ----------------
user_input = st.chat_input("Type your message...")

# ---------------- PROCESS ----------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model='phi',   # fast model
        messages=st.session_state.messages
    )

    ai_reply = response['message']['content']

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.chat_message("assistant").write(ai_reply)
