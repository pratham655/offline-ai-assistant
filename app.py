import streamlit as st
import ollama
from pypdf import PdfReader

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Offline AI Assistant", layout="wide")

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

st.title("🧠 Offline AI Assistant")

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_chunks" not in st.session_state:
    st.session_state.pdf_chunks = []

# ---------------- PDF UPLOAD ----------------
uploaded_file = st.file_uploader("📚 Upload PDF (optional)", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    chunks = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            for i in range(0, len(text), 400):   # smaller = faster
                chunks.append(text[i:i+400])

    st.session_state.pdf_chunks = chunks
    st.success("✅ PDF Ready!")

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ---------------- INPUT ----------------
user_input = st.chat_input("Type your message...")

# ---------------- PROCESS ----------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # ---------- PDF MODE ----------
    if st.session_state.pdf_chunks:
        relevant_chunks = []

        for chunk in st.session_state.pdf_chunks:
            if any(word in chunk.lower() for word in user_input.lower().split()):
                relevant_chunks.append(chunk)

        if not relevant_chunks:
            relevant_chunks = st.session_state.pdf_chunks[:5]

        context = " ".join(relevant_chunks[:3])

        prompt = f"""
        Answer based ONLY on this:

        {context}

        Question: {user_input}
        """

        response = ollama.chat(
            model='phi',
            messages=[{'role': 'user', 'content': prompt}]
        )

    # ---------- NORMAL CHAT ----------
    else:
        response = ollama.chat(
            model='phi',
            messages=st.session_state.messages
        )

    ai_reply = response['message']['content']

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.chat_message("assistant").write(ai_reply)