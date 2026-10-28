"""
Day 42 · Task 3 · Review: Compare: from scratch vs frameworks

Rebuild the core in LangChain or LlamaIndex and compare.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: LangChain RAG =====
# pip install langchain langchain-community langchain-chroma langchain-openai
# Follow the LangChain RAG tutorial, but with YOUR documents from day 38.
# TODO: loader -> RecursiveCharacterTextSplitter -> Chroma vector store -> retriever -> chain


# ===== Part 2: LlamaIndex =====
# pip install llama-index
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# TODO: docs = SimpleDirectoryReader("docs").load_data()
# TODO: index = VectorStoreIndex.from_documents(docs); qe = index.as_query_engine()
# TODO: print(qe.query("..."))


# ===== Part 3: Compare =====
# ## From scratch vs framework
# | | My day 39 code | LangChain | LlamaIndex |
# |-|-|-|-|
# | Lines of code | | | |
# | Easy to debug? | | | |
# | Control over prompt | | | |
#
# What the framework hides:
# -
#
# What I'd keep manual in production:
# -
