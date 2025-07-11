import streamlit as st
from retriever import Retriever
from generator import generate_with_openai, generate_with_huggingface

st.set_page_config(page_title="Loan Approval Chatbot", layout="centered")

# --- Sidebar Configuration ---
st.sidebar.title("🔧 Configuration")
llm_option = st.sidebar.selectbox("Choose LLM", ["OpenAI", "Hugging Face (Mistral)"])
openai_key = None
if llm_option == "OpenAI":
    openai_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")

# --- Load Retriever ---
@st.cache_resource
def load_retriever():
    retriever = Retriever()
    retriever.preprocess_csv("data/Training Dataset.csv")
    retriever.build_index()
    return retriever

retriever = load_retriever()

# --- Main Interface ---
st.title("📊 Loan Approval Q&A Chatbot")
query = st.text_input("Ask a question about the loan data:")

if query:
    with st.spinner("Retrieving relevant information..."):
        docs = retriever.get_top_k(query)
    with st.spinner(f"Generating answer using {llm_option}..."):
        if llm_option == "OpenAI":
            if not openai_key:
                st.error("Please enter your OpenAI API key in the sidebar.")
            else:
                answer = generate_with_openai(docs, query, openai_key)
                st.success("Answer:")
                st.markdown(answer)
        else:
            answer = generate_with_huggingface(docs, query)
            st.success("Answer:")
            st.markdown(answer)

    with st.expander("📄 Retrieved Contexts"):
        for d in docs:
            st.markdown(f"- {d}")
