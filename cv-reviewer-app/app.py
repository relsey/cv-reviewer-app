import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

st.title("Basit CV Değerlendirme Uygulaması")

uploaded_file = st.file_uploader("CV'nizi yükleyin (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("CV başarıyla yüklendi!")
    cv_text = extract_text_from_pdf(uploaded_file)
    st.subheader("CV Metni:")
    st.write(cv_text[:1000])  # İlk 1000 karakteri göster
    # Anahtar kelime listemiz (dilersen genişletebiliriz)
    KEYWORDS = [
        "python", "machine learning", "data analysis", "deep learning",
        "tensorflow", "pandas", "numpy", "scikit-learn", "nlp"
    ]


    def analyze_keywords(cv_text):
        found = []
        missing = []
        text_lower = cv_text.lower()

        for keyword in KEYWORDS:
            if keyword in text_lower:
                found.append(keyword)
            else:
                missing.append(keyword)
        return found, missing