# pccmd-chatbot-llm
Lightweight RAG chatbot for Punjab's PC&amp;CMD using a local JSON knowledge base. Answers user queries via embeddings and similarity search, handles short queries, shows reverse chat history, suggests example questions, and works fully offline with Streamlit—no external LLM API needed.

# 🛠️ PC&CMD RAG Chatbot (Offline JSON-based)

A lightweight Retrieval-Augmented Generation (RAG) chatbot for the **Price Control & Commodity Management Department (PC&CMD), Punjab**.  
The bot runs **fully offline** using a **local JSON knowledge base** (`data.json`) without relying on external LLM APIs.  

---

## 📌 Features
- **Local Knowledge Base:** Uses `data.json` (Q&A format) as the only data source  
- **Embeddings + Similarity Search:** Finds the most relevant context for queries  
- **Handles Short Queries:** Provides direct context even for one/two-word inputs  
- **Reverse Chat History:** Displays full session history in reverse order  
- **Suggested Prompts:** Provides clickable example questions for easy start  
- **Streamlit Interface:** Simple, interactive, and offline-friendly  

---

## 🖼️ Workflow
The architecture is shown below:  

![Workflow](workflow.png)

---

## 📂 Project Structure
