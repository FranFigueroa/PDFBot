import streamlit as st
import pdfplumber

# App title
st.title("PDF BOT")

# Upload PDF Files
uploaded_files = st.file_uploader("Upload your PDFs", type = "pdf", accept_multiple_files = True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"Procesando:{uploaded_file.name} ")
        with pdflumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
                st.write(f"Content extract of PDF {uploaded_fie.naame}: ")
                st.write(text)
