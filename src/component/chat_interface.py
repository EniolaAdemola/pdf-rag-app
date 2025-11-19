"""
Chat interface for the PDF Rag application.
"""
import streamlit as st
from src.utils.rag_chain import create_rag_chain

# 1. Displaying chat history
def display_chat_history():
    """Display the chat history from session state."""
    for i, chat in enumerate(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            st.write(chat["answer"])
            with st.expander("📚 View Source Context"):
                st.write(chat["context"])


# 2. Handling the question
def handle_question(question: str, vectorstore, model: str, temperature: float, k_chunks: int):
    """
    Handle a user question and generate a response.
    
    Args:
        question: The user's question
        vectorstore: The vector store with document embeddings
        model: The model name to use
        temperature: Temperature setting for the model
        k_chunks: Number of chunks to retrieve
    """
    # Display user question
    with st.chat_message("user"):
        st.write(question)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                # Create RAG chain with current settings
                rag_chain, retriever = create_rag_chain(
                    vectorstore,
                    model_name=model,
                    temperature=temperature,
                    k=k_chunks
                )

                # Get relevant documents first for display
                context_docs = retriever.invoke(question)
                
                # Get answer from RAG chain
                answer = rag_chain.invoke(question)

                # Display answer
                st.write(answer)

                # Show source context
                with st.expander("📚 View Source Context"):
                    for idx, doc in enumerate(context_docs):
                        st.markdown(f"**Chunk {idx + 1}:**")
                        st.write(doc.page_content)
                        st.markdown(f"*Page: {doc.metadata.get('page', 'N/A')}*")
                        st.divider()

                # Save to chat history
                st.session_state.chat_history.append({
                    "question": question,
                    "answer": answer,
                    "context": "\n\n".join([f"**Chunk {i+1}** (Page {doc.metadata.get('page', 'N/A')}):\n{doc.page_content}" 
                                           for i, doc in enumerate(context_docs)])
                })

            except Exception as e:
                st.error(f"❌ Error generating answer: {str(e)}")


# 3. Rendering the chat interface
def render_chat_interface(config: dict):
    """
    Render the main chat interface.
    
    Args:
        config: Configuration dictionary from sidebar
    """
    st.header("💬 Ask Questions")
    
    # Display chat history
    display_chat_history()

    # Question input
    question = st.chat_input("Ask a question about the PDF...")

    if question:
        handle_question(
            question=question,
            vectorstore=st.session_state.vectorstore,
            model=config["model"],
            temperature=config["temperature"],
            k_chunks=config["k_chunks"]
        )

    # Clear chat button
    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()



# 4. Render instructions
def render_instructions():
    """Render the instructions page when no PDF is uploaded."""
    st.info("👈 Please upload a PDF file from the sidebar to get started.")
    
    st.markdown("""
    ### How to use this app:
    1. **Enter your OpenAI API key** in the sidebar (or set it in your `.env` file)
    2. **Upload a PDF** document using the file uploader
    3. **Wait** for the document to be processed and indexed
    4. **Ask questions** about the content using the chat interface
    5. **View sources** to see which parts of the document were used to answer
    
    ### Features:
    - ✅ Automatic PDF text extraction and chunking
    - ✅ Vector-based semantic search
    - ✅ Context-aware answers with source citations
    - ✅ Adjustable parameters (chunk size, temperature, etc.)
    - ✅ LangChain integration for tracking (enable LANGCHAIN_TRACING_V2 in .env)
    """)