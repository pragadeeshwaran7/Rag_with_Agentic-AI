import os
from typing import List, Optional

try:
    import chromadb
    from chromadb.utils import embedding_functions
    HAS_CHROMADB = True
except ImportError:
    HAS_CHROMADB = False

from langchain_core.documents import Document


def _get_chroma_client(vector_store_path: str):
    if not HAS_CHROMADB:
        return None
    if not os.path.isdir(vector_store_path):
        os.makedirs(vector_store_path, exist_ok=True)
    client = chromadb.PersistentClient(path=vector_store_path)
    return client


def build_or_load_collection(
    vector_store_path: str,
    collection_name: str,
    embedding_fn,
):
    client = _get_chroma_client(vector_store_path)
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_fn,
    )
    return collection


def upsert_documents(
    vector_store_path: str,
    collection_name: str,
    docs: List[Document],
    embedding_model,
) -> None:
    if not docs:
        return

    collection = build_or_load_collection(
        vector_store_path=vector_store_path,
        collection_name=collection_name,
        embedding_fn=embedding_model,
    )

    ids = []
    texts = []
    metadatas = []

    for idx, doc in enumerate(docs):
        ids.append(str(idx))
        texts.append(doc.page_content)
        metadatas.append(doc.metadata)

    collection.upsert(documents=texts, metadatas=metadatas, ids=ids)


def query_similar(
    vector_store_path: str,
    collection_name: str,
    embedding_model,
    query_text: str,
    top_k: int = 8,
):
    collection = build_or_load_collection(
        vector_store_path=vector_store_path,
        collection_name=collection_name,
        embedding_fn=embedding_model,
    )
    result = collection.query(
        query_texts=[query_text],
        n_results=top_k,
    )
    return result

