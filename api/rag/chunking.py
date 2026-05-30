from typing import List

from langchain_core.documents import Document


def simple_text_chunk(
    docs: List[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 200,
) -> List[Document]:
    """
    Lightweight text splitter that operates on characters. This avoids
    extra dependencies while still giving us usable RAG chunks.
    """
    chunks: List[Document] = []

    for doc in docs:
        text = doc.page_content
        start = 0
        length = len(text)

        while start < length:
            end = min(start + chunk_size, length)
            chunk_text = text[start:end].strip()
            if chunk_text:
                meta = dict(doc.metadata)
                meta["chunk_start"] = start
                meta["chunk_end"] = end
                chunks.append(Document(page_content=chunk_text, metadata=meta))
            if end == length:
                break
            start = max(0, end - chunk_overlap)

    return chunks

