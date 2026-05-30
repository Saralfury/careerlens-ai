import logging
import os
import uvicorn
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware

from extractor import extract_resume_data
from analyzer import analyze
from models import AnalysisResult
from data import ROLE_SKILLS

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="CareerLens AI", version="1.0.0")

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["meta"])
async def health() -> dict:
    return {"status": "ok", "version": "1.0.0"}

@app.get("/roles", tags=["meta"])
async def list_roles() -> dict:
    return {"roles": sorted(ROLE_SKILLS.keys())}

@app.post("/analyze", response_model=AnalysisResult, status_code=status.HTTP_200_OK, tags=["analysis"])
async def analyze_resume(
    file: UploadFile = File(...),
    target_role: str = Form(...)
) -> AnalysisResult:
    content_type = file.content_type or ""
    filename = file.filename or ""
    
    if "pdf" not in content_type.lower() and not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Only PDF files are accepted.")
    
    role_stripped = target_role.strip()
    if not role_stripped:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="target_role must not be empty.")

    try:
        pdf_bytes = await file.read()
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not read the uploaded file.") from exc

    if len(pdf_bytes) == 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Uploaded file is empty.")

    try:
        # LLM dependency removed, API key no longer required
        resume_data = extract_resume_data(pdf_bytes)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Extraction failed")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Resume extraction failed.") from exc

    try:
        result = analyze(resume_data, role_stripped)
    except Exception as exc:
        logger.exception("Analysis failed")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Analysis failed.") from exc

    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)