from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import json
from typing import Dict, Any

from rag.retriever import retrieve_relevant_context
from rag.validator import basic_pattern_check


def get_llm():
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key and gemini_key != "your_gemini_api_key_here":
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-pro-latest",
            google_api_key=gemini_key,
            temperature=0.7,
        )

    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key and groq_key != "your_groq_api_key_here":
        return ChatGroq(
            model_name="llama-3.3-70b-versatile",
            groq_api_key=groq_key,
            temperature=0.7,
        )

    print("WARNING: No valid API Key found. Using dummy LLM output.")
    return None


async def generate_question_paper(
    board: str,
    subject: str,
    difficulty: str,
    pattern: Dict[str, Any],
    is_full_paper: bool,
) -> str:
    """
    Core RAG pipeline: retrieves board/subject-specific academic context from a
    vector-backed knowledge base and uses it, together with the board pattern,
    to generate a novel exam-style question paper.
    """
    llm = get_llm()

    retrieved_docs = retrieve_relevant_context(
        board=board,
        subject=subject,
        difficulty=difficulty,
        pattern=pattern,
    )
    retrieved_context = "\n\n---\n\n".join(
        d.page_content for d in retrieved_docs
    ) if retrieved_docs else "No external notes available; rely on your own knowledge of the syllabus."

    pattern_json = json.dumps(pattern, indent=2)

    prompt_template = """
You are an expert academic content creator and examiner for Class 10 Board Examinations in India.
You must generate a mock question paper for the {board} Board for the subject "{subject}".
The overall difficulty level should be {difficulty}.

You are given two distinct kinds of context:

1) STRICT EXAM PATTERN (must be followed exactly, including sections and marks):
{pattern_json}

2) ACADEMIC CONTENT NOTES (for inspiration only; DO NOT copy sentences or questions verbatim):
{retrieved_context}

Very important requirements:
- Do NOT copy text, sentences, or questions from the academic notes. Always paraphrase and create new questions.
- Preserve the exam-style framing and academic rigor that matches the above board and subject.
- Maintain the cognitive variation (easy/medium/hard) appropriate for the requested "{difficulty}" level.
- Include all general instructions at the top.
- Format the output neatly in Markdown:
  - Use "#", "##", "###" headings appropriately.
  - Use "##" for sections (e.g., "## Section A").
  - Use bold for marks, e.g., **[2 Marks]**.
- Allocate marks exactly as per the structure in the STRICT EXAM PATTERN.
- Include the Time Allowed and Maximum Marks at the very top.

Generate a complete, original question paper below. Do not include any explanations or answers.
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["board", "subject", "difficulty", "pattern_json", "retrieved_context"],
    )

    if not llm:
        return f"""# Mock Question Paper
## {board} Board Examination - {subject}
**Time Allowed:** {pattern.get('time_allowed', '3 Hours')} | **Maximum Marks:** {pattern.get('total_marks', 80)}

### General Instructions:
{chr(10).join(['- ' + inst for inst in pattern.get('general_instructions', [])])}

### Section A
1. This is a generated dummy question because no API key was provided. **[1 Mark]**
"""

    chain = prompt | llm | StrOutputParser()
    result: str = chain.invoke(
        {
            "board": board,
            "subject": subject,
            "difficulty": difficulty,
            "pattern_json": pattern_json,
            "retrieved_context": retrieved_context,
        }
    )

    pattern_ok = basic_pattern_check(pattern, result)
    if pattern_ok and all(pattern_ok.values()):
        return result

    repair_template = """
You previously generated the following question paper for {board} {subject} (difficulty: {difficulty}):

=== ORIGINAL PAPER START ===
{original_paper}
=== ORIGINAL PAPER END ===

The STRICT EXAM PATTERN that must be followed is:
{pattern_json}

Your task:
- Keep the spirit and ideas of the original questions.
- Fix the structure so that it strictly matches the sections and mark allocations in the pattern.
- Do NOT add explanations or answers.
- Maintain originality (do not copy from any source).

Return ONLY the corrected question paper in Markdown.
"""
    repair_prompt = PromptTemplate(
        template=repair_template,
        input_variables=["board", "subject", "difficulty", "original_paper", "pattern_json"],
    )
    repair_chain = repair_prompt | llm | StrOutputParser()
    repaired = repair_chain.invoke(
        {
            "board": board,
            "subject": subject,
            "difficulty": difficulty,
            "original_paper": result,
            "pattern_json": pattern_json,
        }
    )
    return repaired

