"""
PDF processing utilities for the RAG chatbot
"""
import os
import tempfile
from typing import Tuple
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


# Formats docs
def format_docs(docs):
    """
    Format retrieved documents into a single string.
    
    Args:
        docs: List of retrieved documents
        
    Returns:
        str: Formatted string with numbered sources
    """
    return "\n\n".join([f"Source {i+1}:\n{doc.page_content}" for i, doc in enumerate(docs)])

# Process pdf
def process_pdf(pdf_file, chunk_size=1000, chunk_overlap=200) -> Tuple:
    """
    Process uploaded PDF and create a Vector store

    Args:
        pdf_file: Uploaded PDF file
        chunk_size: Size of each chunk
        chunk_overlap: Overlap between chunks

    Returns:
        Tuple(chroma, int): Vector store and number of pages/chunks created
    """
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        tmp_file_path = tmp_file.name

    try:
        # Load PDF
        loader = PyPDFLoader(tmp_file_path)
        documents = loader.load()

        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
        splits = text_splitter.split_documents(documents)

        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(documents=splits, embedding=embeddings, collection_name="pdf_collection")
        return vector_store, len(splits)

    finally:
        # Clean up temporary file
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)