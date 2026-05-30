import re
from typing import Dict


def basic_pattern_check(pattern: dict, generated_markdown: str) -> Dict[str, bool]:
    """
    Very lightweight structural checker to see if key sections from the
    board pattern appear in the generated paper.
    """
    sections = pattern.get("sections", [])
    results: Dict[str, bool] = {}

    for section in sections:
        name = section.get("name")
        if not name:
            continue
        pattern_heading = re.escape(name)
        found = re.search(pattern_heading, generated_markdown, flags=re.IGNORECASE) is not None
        results[name] = found

    return results

