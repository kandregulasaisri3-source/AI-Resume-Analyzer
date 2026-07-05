import streamlit as st
from agent import extract_text, analyze_resume

st.title("AI Resume Analyzer Agent")

uploaded = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if uploaded:

    text = extract_text(uploaded)

    if st.button("Analyze Resume"):

        result = analyze_resume(text)

        st.write(result)