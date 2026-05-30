from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class GenerateRequest(BaseModel):
    board: str
    subject: str
    difficulty: str = "Medium"
    full_paper: bool = True

class GenerateResponse(BaseModel):
    success: bool
    paper_content: str
    board: str
    subject: str
    difficulty: str

class ExportPdfRequest(BaseModel):
    paper_content: str

class BoardInfo(BaseModel):
    id: str
    name: str
    subjects: List[str]
    pattern: Dict[str, Any]
