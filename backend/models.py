from pydantic import BaseModel
from typing import List, Optional

class ResumeData(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    summary: Optional[str] = None
    skills: List[str]
    experience_years: float
    job_titles: List[str]
    education: List[str]
    certifications: List[str]

class RoadmapItem(BaseModel):
    skill: str
    priority: str
    resources: List[str]
    estimated_weeks: int

class AnalysisResult(BaseModel):
    role: str
    fit_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    resume_data: ResumeData
    roadmap: List[RoadmapItem]
    recommendation: str

class AnalyzeRequest(BaseModel):
    target_role: str

class ErrorResponse(BaseModel):
    detail: str