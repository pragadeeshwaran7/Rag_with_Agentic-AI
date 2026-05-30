from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

# Add the api folder to python path for Vercel
sys.path.append(os.path.dirname(__file__))

from pydantic import BaseModel
from dotenv import load_dotenv

# Load env variables
load_dotenv()

from schemas import GenerateRequest, GenerateResponse, ExportPdfRequest, BoardInfo
from board_patterns import get_board_info
from rag_pipeline import generate_question_paper

app = FastAPI(title="AI Question Paper Generator", version="1.0.0")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
@app.get("/")
def health_check():
    return {"status": "ok", "message": "AI Question Paper Generator API is running"}

@app.get("/api/boards")
@app.get("/boards")
def list_boards():
    """Returns available boards and their subjects"""
    # Assuming we have CBSE, ICSE, WB Board
    boards = [
        {"id": "CBSE", "name": "Central Board of Secondary Education", "subjects": ["Mathematics", "Science", "English", "Social Science"]},
        {"id": "ICSE", "name": "Indian Certificate of Secondary Education", "subjects": ["Mathematics", "Science", "English", "History & Civics"]},
        {"id": "WB", "name": "West Bengal Board of Secondary Education", "subjects": ["Mathematics", "Physical Science", "Life Science", "English", "Bengali"]}
    ]
    return {"boards": boards}

@app.post("/api/generate", response_model=GenerateResponse)
@app.post("/generate", response_model=GenerateResponse)
async def generate_paper(request: GenerateRequest):
    try:
        # 1. Fetch Board Pattern
        board_pattern = get_board_info(request.board, request.subject)
        
        if not board_pattern:
            raise HTTPException(status_code=400, detail="Invalid board or subject selected")

        # 2. Invoke RAG Pipeline
        generated_paper = await generate_question_paper(
            board=request.board,
            subject=request.subject,
            difficulty=request.difficulty,
            pattern=board_pattern,
            is_full_paper=request.full_paper
        )

        return GenerateResponse(
            success=True,
            paper_content=generated_paper,
            board=request.board,
            subject=request.subject,
            difficulty=request.difficulty
        )

    except Exception as e:
        print(f"Error generating paper: {e}")
        raise HTTPException(status_code=500, detail=str(e))


