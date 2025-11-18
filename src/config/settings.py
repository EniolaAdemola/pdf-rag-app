"""
Configuration settings for the RAG Chatbot Application
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LangSmith Configuration
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model Option
AVAILABLE_MODELS = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4o"
    "gpt-4o-mini",
]
DEFAULT_MODEL = "gpt-4o-mini"

# RAG Configuration
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200
DEFAULT_TEMPERATURE = 0.3
DEFAULT_K_CHUNKS = 3

# System Prompt
SYSTEM_PROMPT = """You are a helpful assistant answering questions based on the provide context.

Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
Keep your answer short, concise and relevant.

{context}
"""

# UI Configuration
PAGE_TITLE = "PDF Q&A RAG System"
PAGE_ICON = "📚"
APP_TITLE = "📚 PDF Q&A RAG System"
APP_DESCRIPTION = "A simple RAG system for answering questions based on PDF documents."


def setup_environment():
    """
    Set up the environment variables for the application
    """
    os.environ["LANGCHAIN_TRACING_V2"] = LANGCHAIN_TRACING_V2
    if LANGCHAIN_API_KEY:
        os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
    if LANGCHAIN_PROJECT:
        os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT
    if OPENAI_API_KEY:
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # Write a condition that prints tracing status for debugging
    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        print(f"✅ LangSmith Tracing Enabled - Project: {LANGCHAIN_PROJECT}")
    else:
        print("❌ LangSmith Tracing Disabled - Set LANGCHAIN_TRACING_V2=true and LANGCHAIN_API_KEY in .env")
