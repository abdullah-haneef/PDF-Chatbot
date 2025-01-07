# Chat with PDF 📄🤖

**An interactive application** that allows you to:
1. Upload a PDF document.  
2. Extract its text using `pdfplumber`.  
3. Convert text chunks to **OpenAI** embeddings (for semantic understanding).  
4. Store embeddings in a **FAISS** vector store.  
5. Interact with a **Hugging Face** LLM to answer questions about your PDF’s content.  

---

## ✨ Features

- **PDF Upload**: Easily upload any `.pdf` file.  
- **Text Extraction**: Automatically extract text using `pdfplumber`.  
- **Chunking**: Splits large documents into smaller chunks for better context management.  
- **Semantic Search**: Generates embeddings using OpenAI for powerful, context-based retrieval.  
- **LLM Querying**: Leverages Hugging Face Hub (free tier-friendly) to provide answers in plain English.  
- **Contextual Answers**: Retrieves the most relevant chunks from your document to form an accurate, context-aware response.  
- **Bonus**: Expandable section to see which chunks from the PDF were used to form the answer.

---

## 🚀 Quick Start

### Folder Structure

Your project structure should look like this:
chat-with-pdf/
│
├── app.py
├── requirements.txt
├── README.md
└── utils/
    ├── pdf_utils.py
    └── embedding_utils.py


- **`app.py`**: Main Streamlit application.  
- **`requirements.txt`**: Python dependencies.  
- **`README.md`**: This document (setup & usage).  
- **`utils/pdf_utils.py`**: Module to extract text from PDF.  
- **`utils/embedding_utils.py`**: Modules for embedding, vector store creation, and LLM logic.

---

## 🛠 Prerequisites

- **Python 3.8+**  
- **OpenAI API Key** (for embeddings)  
  - [Sign up here](https://platform.openai.com/signup) if you don’t have one yet.  
- **Hugging Face Hub API Token** (for the LLM)  
  - [Sign up for a free account](https://huggingface.co/join) and get your personal access token in your [settings](https://huggingface.co/settings/tokens).  

> **Note**: Store these secrets **securely**. For local testing, you can set environment variables or place them in a `.env` (just don’t commit them to GitHub).

---

## 📦 Installation

1. **Clone** or **download** this repository:
   ```bash
   git clone https://github.com/your-username/chat-with-pdf.git
   cd chat-with-pdf

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Set environment variables for your keys (example using a terminal):
    ```bash
   export OPENAI_API_KEY="your-openai-key"
    export HUGGINGFACEHUB_API_TOKEN="hf_your-huggingface-key"
    ```
   Alternatively, on Windows:
    ```bash
    $env:OPENAI_API_KEY="your-openai-key"
    $env:HUGGINGFACEHUB_API_TOKEN="hf_your-huggingface-key"

4. Verify the environment variables (optional):
    ```bash
   echo $OPENAI_API_KEY
    echo $HUGGINGFACEHUB_API_TOKEN
    ```
    You should see your keys (or an empty line if they’re not set).

## ⚙️ Usage

### Run Through Streamlit Cloud
Streamlit Cloud allows you to deploy your app without hosting infrastructure. Here’s how to do it:

1. Fork or Push this repository to your own GitHub.

2. Go to Streamlit Cloud and sign in with your GitHub account.

3. Create a new app:
- Select your forked repository.
- Choose the app.py file as the entry point.

4. Set secrets on Streamlit Cloud:
- Go to “Settings” in your Streamlit Cloud project.
- Under “Secrets”, add:
    ```bash
   OPENAI_API_KEY="your-openai-key"
    HUGGINGFACEHUB_API_TOKEN="hf_your-huggingface-key"
    ```

5. Deploy the app!

6. Once deployed, Streamlit provides a shareable URL. You can open it in a browser, or send it to friends and colleagues.
That’s it! Now your Chat with PDF app is live on the internet!

Important: Remember to keep your secrets safe—never commit them directly to your public repository.

