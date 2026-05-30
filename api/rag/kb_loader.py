import os
from typing import List, Dict

from langchain_core.documents import Document


def load_kb_documents(
    base_path: str,
    board: str,
    subject: str,
) -> List[Document]:
    """
    Load plain-text or markdown files for a given board/subject from a
    simple folder structure:

        {base_path}/{board}/{subject}/*.txt|*.md

    If no board/subject-specific folder exists, falls back to:
        {base_path}/common/{subject}
        {base_path}/common
    """
    docs: List[Document] = []

    def _collect_from(path: str, metadata: Dict[str, str]) -> None:
        if not os.path.isdir(path):
            return
        for name in os.listdir(path):
            if not (name.endswith(".txt") or name.endswith(".md")):
                continue
            full_path = os.path.join(path, name)
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    text = f.read()
            except OSError:
                continue
            if not text.strip():
                continue
            docs.append(
                Document(
                    page_content=text,
                    metadata={
                        "board": metadata.get("board"),
                        "subject": metadata.get("subject"),
                        "source_path": full_path,
                        "filename": name,
                    },
                )
            )

    # Primary: exact board/subject folder
    _collect_from(
        os.path.join(base_path, board, subject),
        {"board": board, "subject": subject},
    )

    # Fallbacks
    _collect_from(
        os.path.join(base_path, "common", subject),
        {"board": board, "subject": subject},
    )
    _collect_from(
        os.path.join(base_path, "common"),
        {"board": board, "subject": subject},
    )

    return docs

