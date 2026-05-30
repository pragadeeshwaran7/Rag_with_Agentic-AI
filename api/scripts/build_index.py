import os

from rag.kb_loader import load_kb_documents
from rag.chunking import simple_text_chunk
from rag.embeddings import get_embedding_model
from rag.vector_store import upsert_documents


def main() -> None:
    board = os.getenv("INDEX_BOARD", "CBSE")
    subject = os.getenv("INDEX_SUBJECT", "Science")

    kb_base = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")
    vector_store_path = os.getenv("VECTOR_STORE_PATH", "./chroma_db")

    print(f"Building index for board={board}, subject={subject}")
    docs = load_kb_documents(kb_base, board=board, subject=subject)
    if not docs:
        print("No knowledge base documents found. Please add files under:")
        print(f"  {kb_base}/{board}/{subject}")
        return

    chunks = simple_text_chunk(docs)
    embedding_model = get_embedding_model()
    if not embedding_model:
        print("No embedding model configured (missing GEMINI_API_KEY).")
        print("RAG will still work in a degraded mode using raw chunks, but no vector index is built.")
        return

    coll_name = f"{board.lower()}_{subject.lower()}".replace(" ", "_")
    upsert_documents(
        vector_store_path=vector_store_path,
        collection_name=coll_name,
        docs=chunks,
        embedding_model=embedding_model,
    )
    print("Index build complete.")


if __name__ == "__main__":
    main()

