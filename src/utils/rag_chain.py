"""
Rag chain builder utilities
"""

from typing import Tuple
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.config.settings import SYSTEM_PROMPT
from src.utils.pdf_processor import format_docs

# Create a function for chat rag chain
def create_rag_chain(vectorstore, model_name: str="gpt-4o-mini", temperature: float=0.3, k: int=3) -> Tuple:
    """
    Create a rag chain for question answering LCEL

    ARGS:
        vectorstore: Vectorstore
        model_name: Model name
        temperature: detemines the randomness of the model
        K : Number of documents to retrieve

    RETURNS:
        Tuple of rag chain and prompt template
    """

    # create retriever
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})

    # Create LLM
    llm = ChatOpenAI(model=model_name, temperature=temperature)

    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ])

    # Create rag chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain, retriever