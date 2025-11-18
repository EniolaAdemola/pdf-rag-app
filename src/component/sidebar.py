"""
Sidebar UI Component for settings and file upload
"""
import os
import streamlit as st
from src.config.settings import (
    OPENAI_API_KEY,
    AVAILABLE_MODELS,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_TEMPERATURE,
    DEFAULT_K_CHUNKS
)

def render_sidebar():
    """
    Render the sidebar UI component with settings and file upload

    Returns:
        dict: Configuration dictionary with all the settings
    """
    with st.sidebar:
        st.header("⚙️ Settings")

        api_key = st.text_input("OpenAI API Key", value=OPENAI_API_KEY, type="password", help="Enter your OpenAI API key or set it in the .env file")

        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key


        # Model Selection
        model  = st.selectbox("Select Model", AVAILABLE_MODELS, index=0, help="Select the OpenAI model to use for the chat")

        # Advanced settings
        with st.expander("Advanced Settings"):
            chunk_size = st.slider("Chunk Size", min_value=500, max_value=2000, value=DEFAULT_CHUNK_SIZE, help="Size of each chunk in characters")
            chunk_overlap = st.slider("Chunk Overlap", min_value=0, max_value=500, value=DEFAULT_CHUNK_OVERLAP, help="Number of characters to overlap between chunks")
            temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=DEFAULT_TEMPERATURE, help="Temperature for the OpenAI model")
            k_chunks = st.slider("Number of Chunks", min_value=1, max_value=10, value=DEFAULT_K_CHUNKS, help="Number of chunks to use for the chat")

        st.divider()

        # File upload
        st.header("📁 Upload Files")
        uploaded_file = st.file_uploader("Upload files", accept_multiple_files=False, type=["pdf"])

        if uploaded_file:
            st.success(f"✅ Loaded: {uploaded_file.name}")
            st.info(f"Size: {uploaded_file.size / 1024: .2f} KB")
       

    return {
        "api_key": api_key,
        "model": model,
        "chunk_size": chunk_size,
        "chunk_overlap": chunk_overlap,
        "temperature": temperature,
        "k_chunks": k_chunks,
        "uploaded_files": uploaded_file
    }
