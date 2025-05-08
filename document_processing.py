import PyPDF2
import os

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def process_documents(uploaded_files):
    text_data = []
    for uploaded_file in uploaded_files:
        file_content = read_pdf(uploaded_file)
        text_data.append(file_content)
    return text_data

def display_chat_history(chat_history):
    for question, answer in chat_history:
        st.write(f"**You:** {question}")
        st.write(f"**AI:** {answer}")
