import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    """
    Splits the text into smaller chunks for better embedding performance.

    Args:
        text (str): The text to split into chunks.
        chunk_size (int): Desired chunk size in words.
        overlap (int): Number of words to overlap between chunks.

    Returns:
        list: A list of text chunks.
    """
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        chunk = words[start : start + chunk_size]
        chunks.append(" ".join(chunk))
        start += (chunk_size - overlap)

    return chunks


def create_faiss_index(docs, model_name='all-MiniLM-L6-v2'):
    """
    Converts a list of document chunks to embeddings and stores them in a FAISS index.

    Args:
        docs (list[str]): List of document chunks/paragraphs.
        model_name (str): Pretrained SentenceTransformer model name.

    Returns:
        index (faiss.IndexFlatIP): FAISS index with stored embeddings.
        embeddings (np.array): List of embeddings for each doc chunk.
        model (SentenceTransformer): The SentenceTransformer model used.
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(docs, convert_to_numpy=True)
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)  # normalize for cosine sim

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    return index, embeddings, model


def retrieve_relevant_chunks(query, index, embeddings, docs, model_sbert, top_k=3):
    """
    Given a query, retrieves the top_k most similar chunks from the FAISS index.

    Args:
        query (str): User's query.
        index (faiss.IndexFlatIP): FAISS index.
        embeddings (np.array): Numpy array of stored embeddings.
        docs (list[str]): Original text chunks.
        model_sbert (SentenceTransformer): SBERT model for generating query embeddings.
        top_k (int): Number of closest chunks to retrieve.

    Returns:
        list[str]: The most relevant text chunks to the query.
    """
    # Encode the query
    query_embedding = model_sbert.encode([query], convert_to_numpy=True)
    query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

    # Search in FAISS
    distances, indices = index.search(query_embedding, top_k)

    best_chunks = []
    for idx in indices[0]:
        best_chunks.append(docs[idx])
    return best_chunks
