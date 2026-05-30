"""
Scrape public syllabus / study-guide pages and save cleaned text into
backend/knowledge_base/{BOARD}/{SUBJECT}/.

Usage (from backend/):
    python -m scripts.scrape_kb
    python -m scripts.scrape_kb --board CBSE --subject Science
"""

from __future__ import annotations

import argparse
import os
import re
import time
from html import unescape
from typing import Dict, List, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# (board, subject) -> list of (filename_slug, url)
SCRAPE_TARGETS: Dict[Tuple[str, str], List[Tuple[str, str]]] = {
    ("CBSE", "Science"): [
        ("syllabus_overview", "https://www.ncertbooks.net/cbse/class-10-science-syllabus/"),
        ("unit_chemistry", "https://infinitylearn.com/cbse-board/class-10-science-syllabus"),
    ],
    ("CBSE", "Mathematics"): [
        ("syllabus_overview", "https://www.ncertbooks.net/cbse/class-10-maths-syllabus/"),
    ],
    ("CBSE", "Social Science"): [
        ("syllabus_overview", "https://www.ncertbooks.net/cbse/class-10-social-science-syllabus/"),
    ],
    ("CBSE", "English"): [
        ("syllabus_overview", "https://www.ncertbooks.net/cbse/class-10-english-syllabus/"),
    ],
    ("ICSE", "Science"): [
        ("syllabus_overview", "https://www.collegedekho.com/icse-class-10-science-syllabus-brd"),
    ],
    ("ICSE", "Mathematics"): [
        ("syllabus_overview", "https://www.collegedekho.com/icse-class-10-math-syllabus-brd"),
        ("syllabus_chapters", "https://www.futuretopper.in/icse-and-isc/class-10-mathematics-syllabus"),
    ],
    ("ICSE", "English"): [
        ("syllabus_overview", "https://www.collegedekho.com/icse-class-10-english-syllabus-brd"),
    ],
    ("ICSE", "History & Civics"): [
        ("syllabus_overview", "https://www.collegedekho.com/icse-class-10-history-syllabus-brd"),
    ],
    ("WB", "Physical Science"): [
        ("syllabus_overview", "https://getmyuni.com/boards/west-bengal-madhyamik-syllabus"),
        ("syllabus_shiksha", "https://www.shiksha.com/boards/wbbse-board-syllabus"),
    ],
    ("WB", "Life Science"): [
        ("syllabus_overview", "https://getmyuni.com/boards/west-bengal-madhyamik-syllabus"),
        ("syllabus_shiksha", "https://www.shiksha.com/boards/wbbse-board-syllabus"),
    ],
    ("WB", "Mathematics"): [
        ("syllabus_overview", "https://getmyuni.com/boards/west-bengal-madhyamik-syllabus"),
        ("syllabus_shiksha", "https://www.shiksha.com/boards/wbbse-board-syllabus"),
    ],
    ("WB", "English"): [
        ("syllabus_overview", "https://getmyuni.com/boards/west-bengal-madhyamik-syllabus"),
        ("syllabus_shiksha", "https://www.shiksha.com/boards/wbbse-board-syllabus"),
    ],
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; QuestionPaperGeneratorBot/1.0; "
        "+https://github.com/edu-rag-kb)"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-IN,en;q=0.9",
}

MIN_CHARS = 400


def kb_root() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "knowledge_base")
    )


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
        tag.decompose()

    main = soup.find("article") or soup.find("main") or soup.body
    if not main:
        return ""

    lines: List[str] = []
    for el in main.find_all(["h1", "h2", "h3", "h4", "p", "li", "td", "th"]):
        text = unescape(el.get_text(separator=" ", strip=True))
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) < 3:
            continue
        if el.name in ("h1", "h2", "h3", "h4"):
            level = int(el.name[1])
            lines.append("#" * level + " " + text)
        elif el.name == "li":
            lines.append(f"- {text}")
        else:
            lines.append(text)

    body = "\n\n".join(lines)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def fetch_page(url: str, timeout: int = 25) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def save_document(
    board: str,
    subject: str,
    slug: str,
    url: str,
    content: str,
) -> str:
    out_dir = os.path.join(kb_root(), board, subject)
    os.makedirs(out_dir, exist_ok=True)

    header = (
        f"# {board} Class 10 — {subject}\n\n"
        f"Source: {url}\n"
        f"Retrieved for RAG knowledge base (syllabus & topic reference).\n\n"
        "---\n\n"
    )
    path = os.path.join(out_dir, f"{slug}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + content)
    return path


def scrape_pair(board: str, subject: str, targets: List[Tuple[str, str]]) -> int:
    saved = 0
    for slug, url in targets:
        try:
            print(f"  Fetching {url} ...")
            html = fetch_page(url)
            text = html_to_text(html)
            if len(text) < MIN_CHARS:
                print(f"    Skipped (too short: {len(text)} chars)")
                continue
            # For WB shared page, tag content by subject in filename only
            if board == "WB" and slug == "syllabus_overview":
                text = _filter_wb_subject(text, subject)
            path = save_document(board, subject, slug, url, text)
            print(f"    Saved -> {path} ({len(text)} chars)")
            saved += 1
            time.sleep(1.2)
        except Exception as exc:
            print(f"    Failed: {exc}")
    return saved


def _filter_wb_subject(text: str, subject: str) -> str:
    """Keep relevant section when one URL covers multiple WB subjects."""
    markers = {
        "Physical Science": [
            "Physical Science",
            "Current Electricity",
            "Metallurgy",
            "Behaviour of Gases",
        ],
        "Life Science": [
            "Life Science",
            "Control and Coordination",
            "Continuity of life",
            "Heredity",
        ],
        "Mathematics": ["Mathematics", "Algebra", "Geometry", "Trigonometry"],
        "English": ["English", "Grammar", "Composition"],
    }
    keys = markers.get(subject, [])
    if not keys:
        return text
    paragraphs = text.split("\n\n")
    kept = [p for p in paragraphs if any(k.lower() in p.lower() for k in keys)]
    if len(kept) >= 3:
        return "\n\n".join(kept)
    return text


def write_curated_fallbacks() -> int:
    """Write structured syllabus notes when scraping fails or is thin."""
    from scripts.kb_curated_content import CURATED_DOCUMENTS

    count = 0
    for board, subject, slug, body in CURATED_DOCUMENTS:
        path = os.path.join(kb_root(), board, subject, f"{slug}.md")
        if os.path.isfile(path) and os.path.getsize(path) > 500:
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        print(f"  Curated -> {path}")
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--board", default=None)
    parser.add_argument("--subject", default=None)
    parser.add_argument("--curated-only", action="store_true")
    args = parser.parse_args()

    print("Writing curated syllabus documents...")
    write_curated_fallbacks()

    if args.curated_only:
        return

    print("\nScraping web sources...")
    total = 0
    for (board, subject), urls in SCRAPE_TARGETS.items():
        if args.board and board != args.board:
            continue
        if args.subject and subject != args.subject:
            continue
        print(f"\n[{board} / {subject}]")
        total += scrape_pair(board, subject, urls)

    print(f"\nDone. Saved {total} scraped file(s) under {kb_root()}")


if __name__ == "__main__":
    main()
