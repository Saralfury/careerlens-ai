import os
import difflib
import joblib
import pandas as pd
from models import ResumeData, AnalysisResult, RoadmapItem
from data import ROLE_SKILLS, ROADMAP_RESOURCES, DEFAULT_RESOURCE

# Pre-load ML artifacts globally for 0-latency inference
MODEL_PATH = os.path.join(os.path.dirname(__file__), "xgboost_model.pkl")
FEATURES_PATH = os.path.join(os.path.dirname(__file__), "feature_columns.pkl")

ML_MODEL = None
FEATURE_COLS = None

if os.path.exists(MODEL_PATH) and os.path.exists(FEATURES_PATH):
    ML_MODEL = joblib.load(MODEL_PATH)
    FEATURE_COLS = joblib.load(FEATURES_PATH)

def _normalise(skill: str) -> str:
    return skill.lower().strip()

def _fuzzy_match(candidate: str, targets: list[str], threshold: float = 0.82) -> str | None:
    matches = difflib.get_close_matches(candidate, targets, n=1, cutoff=threshold)
    return matches[0] if matches else None

def _match_skills(resume_skills: list[str], required_skills: list[str]) -> tuple[list[str], list[str]]:
    norm_resume = [_normalise(s) for s in resume_skills]
    norm_required = [_normalise(s) for s in required_skills]
    matched, missing = [], []

    for req in norm_required:
        if req in norm_resume or any(req in rs or rs in req for rs in norm_resume) or _fuzzy_match(req, norm_resume):
            matched.append(req)
        else:
            missing.append(req)
    return matched, missing

def _assign_priority(idx: int, total_missing: int) -> str:
    if total_missing == 0: return "low"
    third = max(1, total_missing // 3)
    if idx < third: return "high"
    elif idx < third * 2: return "medium"
    return "low"

def _build_roadmap(missing_skills: list[str]) -> list[RoadmapItem]:
    items = []
    total = len(missing_skills)
    for idx, skill in enumerate(missing_skills):
        resource_data = ROADMAP_RESOURCES.get(skill, DEFAULT_RESOURCE)
        items.append(RoadmapItem(
            skill=skill, priority=_assign_priority(idx, total),
            resources=resource_data["resources"], estimated_weeks=resource_data["estimated_weeks"],
        ))
    return items

def _recommendation(score: int) -> str:
    if score >= 80: return "Strong match! You meet most of the requirements for this role. Focus on polishing the few missing skills to make your profile outstanding."
    elif score >= 60: return "Good foundation. You have solid relevant skills but a few important gaps remain. Work through the high-priority roadmap items to become highly competitive."
    elif score >= 40: return "Moderate match. You have transferable skills but will need dedicated upskilling before applying. Follow the full roadmap — 3-6 months of focused effort should get you there."
    else: return "Significant skills gap for this specific role. Consider targeting a more junior level position first, or invest 6-12 months following the roadmap before applying."

def _resolve_role(target_role: str) -> tuple[str, list[str]]:
    norm = _normalise(target_role)
    if norm in ROLE_SKILLS: return norm, ROLE_SKILLS[norm]
    for key in ROLE_SKILLS:
        if norm in key or key in norm: return key, ROLE_SKILLS[key]
    hit = _fuzzy_match(norm, list(ROLE_SKILLS.keys()), threshold=0.7)
    if hit: return hit, ROLE_SKILLS[hit]
    first_key = next(iter(ROLE_SKILLS))
    return first_key, ROLE_SKILLS[first_key]

def _predict_ml_score(resume_skills: list[str], target_role: str, experience_years: float) -> int:
    """Transforms resume data into a feature vector and runs XGBoost inference."""
    # Initialize zero-vector matching training geometry
    feature_dict = {col: 0 for col in FEATURE_COLS}
    
    # Inject continuous feature
    if "experience_years" in feature_dict:
        feature_dict["experience_years"] = experience_years
        
    # Inject one-hot role feature
    role_col = f"target_role_{target_role}"
    if role_col in feature_dict:
        feature_dict[role_col] = 1
        
    # Inject binary skill features
    norm_resume = [_normalise(s) for s in resume_skills]
    for skill in norm_resume:
        if skill in feature_dict:
            feature_dict[skill] = 1
            
    df_features = pd.DataFrame([feature_dict])
    raw_prediction = ML_MODEL.predict(df_features)[0]
    return max(0, min(100, int(round(raw_prediction))))

def analyze(resume_data: ResumeData, target_role: str) -> AnalysisResult:
    resolved_role, required_skills = _resolve_role(target_role)
    matched, missing = _match_skills(resume_data.skills, required_skills)
    
    if ML_MODEL is not None and FEATURE_COLS is not None:
        score = _predict_ml_score(resume_data.skills, resolved_role, resume_data.experience_years)
    else:
        # Failsafe if train_model.py hasn't been executed yet
        skill_score = round((len(matched) / len(required_skills)) * 70) if required_skills else 0
        exp_bonus = min(30, round((resume_data.experience_years / 8) * 30))
        score = max(0, min(100, skill_score + exp_bonus))
        
    return AnalysisResult(
        role=resolved_role,
        fit_score=score,
        matched_skills=sorted(matched),
        missing_skills=sorted(missing),
        resume_data=resume_data,
        roadmap=_build_roadmap(missing),
        recommendation=_recommendation(score),
    )