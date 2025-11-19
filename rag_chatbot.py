"""
PDF Q&A RAG Chatbot - Main Application
"""
import streamlit as st
from src.config.settings import PAGE_TITLE, PAGE_ICON, APP_TITLE, APP_DESCRIPTION, setup_environment
from src.component.sidebar import render_sidebar
from src.component.chat_interface import render_chat_interface, render_instructions
from src.utils.pdf_processor import process_pdf

# Set up the environment
setup_environment()

def main():
    """Main  application entry point"""

    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

    st.title(APP_TITLE)
    st.write(APP_DESCRIPTION)

    # Render sidebar and get config
    config = render_sidebar()

    # main content area
    if not config["api_key"]:
        st.warning("⚠️Please enter your OpenAI API key in the sidebar to continue.")
        return

    # Initialize our session state
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "processed_file" not in st.session_state:
        st.session_state.processed_file = None

    # Process PDF when uploaded
    # uploaded_file = config.get("uploaded_file", None)
    uploaded_file = config.get("uploaded_file", None)
    # uploaded_file = config["uploaded_file"]
    if uploaded_file and st.session_state.processed_file != uploaded_file.name:
        with st.spinner("🔄 Processing PDF... This may take a moment."):
            try:
                vectorstore, num_chunks = process_pdf(
                    uploaded_file,
                    chunk_size=config["chunk_size"],
                    chunk_overlap=config["chunk_overlap"]
                )
                st.session_state.vectorstore = vectorstore
                st.session_state.processed_file = uploaded_file.name
                st.session_state.chat_history = []  # Reset chat history
                st.success(f"✅ PDF processed successfully! Created {num_chunks} chunks.")
            except Exception as e:
                st.error(f"❌ Error processing PDF: {str(e)}")
                st.stop()

    # Display chat interface or instructions
    if st.session_state.vectorstore:
        render_chat_interface(config)
    else:
        render_instructions()


if __name__ == "__main__":
    main()