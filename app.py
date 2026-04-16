import streamlit as st
from utils.ocr import extract_text_from_image
from utils.extractor import extract_fields

st.set_page_config(page_title="AI Document Scanner", layout="wide")

st.title("📄 AI Document Scanner + OCR")

st.write("Upload a document (receipt, invoice, etc.) to extract structured data using AI.")

uploaded_file = st.file_uploader("Upload Document Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # OCR extraction
    with st.spinner("Extracting text..."):
        text = extract_text_from_image(uploaded_file)

    st.subheader("📝 Extracted Text")
    st.text_area("OCR Output", text, height=200)

    # LLM extraction
    if st.button("🤖 Extract Structured Data"):
        with st.spinner("Processing with AI..."):
            structured_data = extract_fields(text)

        st.subheader("📊 Extracted Data (JSON)")
        st.json(structured_data)
