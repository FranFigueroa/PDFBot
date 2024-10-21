import streamlit as st
import pdfplumber
from langchain.text_splitter import CharacterTextSplitter

# App title
st.title("PDF BOT")


# Text Splitter function
def split_text(text, chunk_size = 1000, chunk_overlap = 200):
    splitter = CharacterTextSplitter(
        separator = "", # Divide for words
        chunk_size = chunk_size, # Chunk size
        chunk_overlap = chunk_overlap, # Superposition between chunks
        length_function = len
            )
    chunks = splitter.split_text(text)
    return chunks

# Upload PDF Files
uploaded_files = st.file_uploader("Upload your PDFs", type = "pdf", accept_multiple_files = True)


if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"Processing: {uploaded_file.name}")
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            
            st.write(f"Conteth of PDF {uploaded_file.name}:")

            # Dividir el texto en fragmentos
            chunks = split_text(text)
            st.write(f" The text has been divideded into {len(chunks)} chunks.")
            
            # Mostrar algunos fragmentos
            for i, chunk in enumerate(chunks[:5]):  # Show some initial chunks
                st.write(f"Chunks {i+1}:")
                st.write(chunk)
