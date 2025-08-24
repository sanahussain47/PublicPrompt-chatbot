import streamlit as st
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random

# ------------------------------
# Force CPU device to avoid meta tensor error
# ------------------------------
device = "cpu"

# ------------------------------
# Load JSON knowledge base
# ------------------------------
with open("data.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

questions = [item["question"] for item in knowledge_base]
answers = [item["answer"] for item in knowledge_base]

# ------------------------------
# Embedding model for similarity search
# ------------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2", device=device)
question_embeddings = embedder.encode(questions, convert_to_tensor=True)

# ------------------------------
# Function to retrieve most relevant context (top_k)
# ------------------------------
def retrieve_context(user_query, top_k=3):
    query_embedding = embedder.encode([user_query], convert_to_tensor=True)
    similarities = cosine_similarity(query_embedding.cpu(), question_embeddings.cpu())[0]
    top_idx = np.argsort(similarities)[-top_k:][::-1]  # top k indices
    best_idx = top_idx[0]
    return answers[best_idx]

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="PCCMD Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 PCCMD Chatbot")
st.write("Ask me about Price Control & Commodity Management!")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "question" not in st.session_state:
    st.session_state["question"] = ""

# ------------------------------
# Sidebar: Suggested Questions
# ------------------------------
st.sidebar.header("💡 Example Questions")
for q in random.sample(questions, min(10, len(questions))):
    if st.sidebar.button(q):
        st.session_state["question"] = q

# ------------------------------
# Main Input
# ------------------------------
user_query = st.text_input("Your Question:", value=st.session_state.get("question", ""))

if st.button("Get Answer") and user_query.strip():
    answer = retrieve_context(user_query)
    
    # Add to chat history (latest first)
    st.session_state["chat_history"].insert(0, {"question": user_query, "answer": answer})
    st.session_state["question"] = ""  # reset input

# ------------------------------
# Display chat history (reverse order)
# ------------------------------
if st.session_state["chat_history"]:
    st.subheader("💬 Chat History")
    for chat in st.session_state["chat_history"]:
        st.markdown(f"**Q:** {chat['question']}")
        st.markdown(f"**A:** {chat['answer']}")
        st.markdown("---")
