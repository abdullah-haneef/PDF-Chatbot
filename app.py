import streamlit as st
import os

from pdf_utils import extract_text_from_pdf
from embedding_utils import (
    chunk_text,
    create_faiss_index,
    retrieve_relevant_chunks
)
from openai_utils import answer_question_with_chat_gpt


def main():
    st.title("PDF Q&A with GPT")

    # 1. Prompt user for OpenAI API Key
    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key to proceed.")
        st.stop()

    # 2. File Uploader
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file is None:
        st.info("Please upload a PDF file to begin.")
        st.stop()

    # 3. Extract text from PDF
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF text extracted successfully!")

    # 4. Chunk the text
    with st.spinner("Chunking text..."):
        chunks = chunk_text(pdf_text, chunk_size=100, overlap=20)
    st.write(f"**Number of chunks created:** {len(chunks)}")

    # 5. Create embeddings + FAISS index
    with st.spinner("Creating embeddings and building FAISS index..."):
        index, embeddings, model_sbert = create_faiss_index(chunks, model_name='all-MiniLM-L6-v2')
    st.success("Embeddings created and FAISS index built!")

    # 6. Q&A Section
    st.write("---")
    st.subheader("Ask a Question about the PDF")

    # We'll keep a session state to store conversation if needed
    if "user_question" not in st.session_state:
        st.session_state.user_question = ""

    # Input
    user_question = st.text_input("Your Question", key="user_question")

    if user_question:
        with st.spinner("Retrieving relevant chunks..."):
            relevant_chunks = retrieve_relevant_chunks(
                user_question, index, embeddings, chunks, model_sbert, top_k=3
            )
        combined_context = "\n".join(relevant_chunks)

        # 7. Use GPT to get an answer
        with st.spinner("Generating answer..."):
            try:
                answer = answer_question_with_chat_gpt(
                    user_question,
                    combined_context,
                    openai_api_key=openai_api_key,
                    model="gpt-3.5-turbo"
                )
                st.write("**Answer:**")
                st.write(answer)
            except Exception as e:
                st.error(f"OpenAI API Error: {e}")


if __name__ == "__main__":
    main()
