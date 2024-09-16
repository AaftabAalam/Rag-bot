import streamlit as st
import ollama
from PyPDF2 import PdfReader

st.title("💬 Mistral-OpenOrca PDF Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you with the content of the uploaded PDFs?"}]

if "documents" not in st.session_state:
    st.session_state["documents"] = {}

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        extracted_text = ""
        for page in reader.pages:
            if page.extract_text():
                extracted_text += page.extract_text()
        return extracted_text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""

def add_documents():
    uploaded_files = st.file_uploader("Upload PDF documents", accept_multiple_files=True, type=["pdf"])
    if uploaded_files:
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            if text:
                st.session_state["documents"][file.name] = text
        st.success("Documents uploaded and processed successfully.")

def find_relevant_documents(query):
    relevant_docs = []
    query_keywords = set(query.lower().split())  # Split the query into keywords
    for doc_name, doc_text in st.session_state["documents"].items():
        # Check if any of the query keywords are present in the document
        if any(keyword in doc_text.lower() for keyword in query_keywords):
            relevant_docs.append(doc_text)
    return relevant_docs

def generate_response_from_documents(context, query):
    # This function generates responses strictly based on the context from the documents.
    messages = [{"role": "system", "content": f"Context: {context}"}, {"role": "user", "content": query}]
    response = ollama.chat(model='mistral-openorca', stream=True, messages=messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

add_documents()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

if prompt := st.chat_input("Ask a question related to the uploaded PDF documents"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    relevant_documents = find_relevant_documents(prompt)

    if relevant_documents:
        context = "\n".join(relevant_documents)
        st.session_state["full_message"] = ""
        st.chat_message("user", avatar="🧑‍💻").write(prompt)
        st.chat_message("assistant", avatar="🤖").write_stream(generate_response_from_documents(context, prompt))
        st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
    else:
        # If no relevant document is found, inform the user
        response_message = "No relevant information found in the uploaded PDFs."
        st.chat_message("assistant", avatar="🤖").write(response_message)
        st.session_state.messages.append({"role": "assistant", "content": response_message})
