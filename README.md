# PDF Q&A RAG System

## Overview

The **PDF Q&A RAG System** is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content. The system processes the uploaded PDF, splits it into chunks, and uses OpenAI's language models to provide context-aware answers with source citations.

## Features

- **PDF Upload and Processing**: Extracts text from uploaded PDFs and splits them into manageable chunks.
- **Vector-Based Semantic Search**: Uses embeddings to retrieve relevant document chunks.
- **Context-Aware Answers**: Provides answers based on the content of the uploaded PDF.
- **Customizable Settings**: Adjust chunk size, overlap, temperature, and more.
- **Source Citations**: Displays the document chunks used to generate answers.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/EniolaAdemola/pdf-rag-app.git
   cd pdf-rag-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with the following variables:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run rag_chatbot.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Upload a PDF file using the sidebar and start asking questions!

## Project Structure

```
.
├── rag_chatbot.py          # Main application entry point
├── requirements.txt        # Python dependencies
├── src/                    # Source code
│   ├── component/          # UI components (sidebar, chat interface)
│   ├── config/             # Configuration settings
│   ├── utils/              # Utility functions (PDF processing, RAG chain)
├── .env                    # Environment variables (not included in repo)
└── README.md               # Project documentation
```

## Technologies Used

- **Streamlit**: For building the web interface.
- **LangChain**: For creating the RAG chain and managing document embeddings.
- **OpenAI API**: For generating answers using GPT models.
- **Chroma**: For vector storage and retrieval.
- **PyPDF**: For extracting text from PDF files.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

### Project Overview

<img width="1917" height="1117" alt="image" src="https://github.com/user-attachments/assets/4b086a5f-f7f0-4719-a303-9a93965e765d" />
