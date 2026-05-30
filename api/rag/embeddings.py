import os
from typing import Optional

from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embedding_model() -> Optional[GoogleGenerativeAIEmbeddings]:
    """
    Returns a Google Gemini embeddings model if GEMINI_API_KEY is set,
    otherwise None. The caller should fall back to non-vector retrieval
    strategies if this returns None.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        return None

    return GoogleGenerativeAIEmbeddings(
        model="text-embedding-004",
        google_api_key=api_key,
    )

