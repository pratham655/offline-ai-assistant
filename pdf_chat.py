import streamlit as st
import ollama
from pypdf import PdfReader

st.set_page_config(page_title="Smart PDF AI Assistant", layout="wide")

st.title("📚 Smart PDF AI Assistant")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    chunks = []

    # 🔹 Split PDF into chunks
    for page in reader.pages:
        text = page.extract_text()
        if text:
            for i in range(0, len(text), 500):
                chunks.append(text[i:i+500])

    st.success("PDF Loaded & Processed!")

    question = st.text_input("Ask a question:")

    if question:
        relevant_chunks = []

        # 🔹 Improved keyword matching
        for chunk in chunks:
            for word in question.lower().split():
                if word in chunk.lower():
                    relevant_chunks.append(chunk)
                    break

        # 🔹 Fallback
        if not relevant_chunks:
            relevant_chunks = chunks[:5]

        # 🔹 Create context
        context = " ".join(relevant_chunks[:3])

        # 🔹 Prompt
        prompt = f"""
        Answer based ONLY on this content:

        {context}

        Question: {question}
        """

        # 🔹 AI Response
        response = ollama.chat(
            model='phi',   # use 'mistral' if you want better quality but slower
            messages=[{'role': 'user', 'content': prompt}]
        )

        st.write("### Answer:")
        st.write(response['message']['content'])