# 🧠 Offline AI Assistant

An intelligent offline AI chatbot with PDF-based question answering built using Streamlit and Ollama.  
This application runs locally without requiring continuous internet access and allows users to interact with AI and extract information from documents.

---

## 🚀 Features

- Offline Chatbot – Interact with AI without internet  
- PDF Question Answering – Upload notes and ask questions  
- Context-Aware Responses – Maintains conversation history  
- Clean UI – Built using Streamlit  
- Optimized Performance – Uses lightweight local model (phi)  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Ollama (Local LLM)  
- pypdf  

---

## ⚙️ How It Works

1. User enters a query  
2. If a PDF is uploaded:
   - Text is extracted and split into chunks  
   - Relevant content is selected based on the query  
   - AI answers using only that context  
3. Otherwise:
   - AI responds using chat history  

---

## ▶️ Run Locally

Step 1: Install dependencies  
pip install -r requirements.txt  

Step 2: Run the app  
python -m streamlit run app.py  

Step 3: Start chatting  
- Ask general questions  
- Upload PDFs and query them  

---

## ⚠️ Note

- This project uses Ollama, so the AI model runs locally  
- Internet is required only for initial setup (model download)  
- Voice feature was explored but removed due to PyAudio compatibility issues with Python 3.13  

---

## 📈 Future Improvements

- Semantic search (FAISS / embeddings)  
- Voice assistant integration  
- Web deployment with cloud models  
- Mobile-friendly UI  

