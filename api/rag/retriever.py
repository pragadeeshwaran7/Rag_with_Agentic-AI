import os
from typing import List

from langchain_core.documents import Document

from .kb_loader import load_kb_documents
from .chunking import simple_text_chunk
from .embeddings import get_embedding_model
from .vector_store import upsert_documents, query_similar


def _collection_name(board: str, subject: str) -> str:
    return f"{board.lower()}_{subject.lower()}".replace(" ", "_")


def retrieve_relevant_context(
    board: str,
    subject: str,
    difficulty: str,
    pattern: dict,
    max_chunks: int = 8,
) -> List[Document]:
    """
    Retrieves semantically relevant chunks for a given board/subject/difficulty.
    If no embeddings model is configured, returns raw documents (non-vector fallback).
    """
    vector_store_path = os.getenv("VECTOR_STORE_PATH", "./chroma_db")
    kb_base = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")

    raw_docs = load_kb_documents(
        base_path=kb_base,
        board=board,
        subject=subject,
    )
    if not raw_docs:
        return []

    chunks = simple_text_chunk(raw_docs)

    embedding_model = get_embedding_model()
    if not embedding_model:
        return chunks[:max_chunks]

    coll_name = _collection_name(board, subject)
    upsert_documents(
        vector_store_path=vector_store_path,
        collection_name=coll_name,
        docs=chunks,
        embedding_model=embedding_model,
    )

    query = (
        f"Class 10 {board} {subject} questions, difficulty {difficulty}, "
        f"matching this pattern: {pattern.get('sections', [])}"
    )
    result = query_similar(
        vector_store_path=vector_store_path,
        collection_name=coll_name,
        embedding_model=embedding_model,
        query_text=query,
        top_k=max_chunks,
    )

    docs: List[Document] = []
    for text, metadata in zip(
        result.get("documents", [[]])[0],
        result.get("metadatas", [[]])[0],
    ):
        docs.append(Document(page_content=text, metadata=metadata or {}))

    return docs

