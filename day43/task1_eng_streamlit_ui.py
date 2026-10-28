"""
Day 43 · Task 1 · Engineering: Streamlit UI

Upload PDFs, ask questions, show sources.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# pip install streamlit    Run: streamlit run day43/task1_ui.py
import requests
import streamlit as st

st.title("Chat with your docs")

uploaded = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
# TODO: send uploaded files to your FastAPI /ingest endpoint

question = st.text_input("Ask a question")
if question:
    # TODO: call FastAPI /ask, show the answer and the sources (st.expander per source)
    pass
