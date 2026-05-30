# AI-Powered Question Paper Generator

A full-stack AI-powered Question Paper Generator using a Retrieval-Augmented Generation (RAG) architecture that generates mock Class 10 Board Examination question papers following the exact pattern and difficulty level of real board exams (CBSE, ICSE, West Bengal Board).

## Architecture

- **Backend**: FastAPI + Python
- **AI Core**: LangChain + Google Gemini Pro (1.5) / Groq
- **Retrieval (RAG)**: ChromaDB + custom knowledge base per board/subject
- **Frontend**: React + Vite + Tailwind CSS

The system uses two kinds of context:

- A **strict pattern knowledge base** (`board_patterns.py`) to enforce sections and mark distributions.
- A **RAG knowledge base** (per board/subject) stored in a vector database (ChromaDB). The LLM retrieves relevant academic content and then generates **novel** questions that match real exam style without copying text verbatim.

## Setup Instructions

### 1. Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (if not already created):
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure Environment Variables:
   Rename `.env.example` to `.env` and add your `GEMINI_API_KEY`.
   *(If you don't add a key, the backend will gracefully fallback to a dummy generated paper for UI testing).*
5. (Optional but recommended) Build the RAG index for a board/subject:

   Place plain-text or markdown notes under:
   - `backend/knowledge_base/CBSE/Science/*.txt|*.md` (and similar for other boards/subjects).

   Then run:
   ```bash
   # From backend/
   set INDEX_BOARD=CBSE
   set INDEX_SUBJECT=Science
   python -m scripts.build_index
   ```

6. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### 2. Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

### 3. Usage
Open the frontend URL (usually `http://localhost:5173`) in your browser. Select a board, subject, and difficulty level, and click "Generate". Once the paper is generated, you can preview it and click "Export as PDF" to download it.
