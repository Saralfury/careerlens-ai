import re
import logging
import fitz  # PyMuPDF

from models import ResumeData
from data import ROLE_SKILLS

logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract text from uploaded PDF.
    """
    text_parts = []

    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text_parts.append(page.get_text())

    except Exception as exc:
        logger.exception("Failed to read PDF")
        raise ValueError("Invalid PDF file.") from exc

    text = "\n".join(text_parts).strip()

    if not text:
        raise ValueError(
            "The uploaded PDF contains no extractable text."
        )

    return text


def _extract_skills(text: str) -> list[str]:
    """
    Extract known skills from resume text.
    """
    text_lower = text.lower()
    found_skills = set()

    all_known_skills = set()

    for skills in ROLE_SKILLS.values():
        all_known_skills.update(skills)

    for skill in all_known_skills:
        skill_lower = skill.lower()

        # Handles C++, C#, Node.js, Next.js etc.
        pattern = rf"(?<!\w){re.escape(skill_lower)}(?!\w)"

        if re.search(pattern, text_lower, flags=re.IGNORECASE):
            found_skills.add(skill)

    return sorted(found_skills)


def _extract_email(text: str) -> str | None:
    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else None


def _extract_phone(text: str) -> str | None:
    match = re.search(
        r"\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}",
        text
    )

    if match:
        digits = re.sub(r"\D", "", match.group(0))

        if len(digits) >= 10:
            return match.group(0).strip()

    return None


def _extract_name(text: str) -> str:
    """
    Best-effort name extraction.
    """
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for line in lines[:5]:
        words = line.split()

        if (
            2 <= len(words) <= 4
            and len(line) < 40
            and not any(char.isdigit() for char in line)
            and "resume" not in line.lower()
        ):
            return line

    return lines[0] if lines else "Unknown Candidate"


def _extract_education(text: str) -> list[str]:
    """
    Extract likely education entries.
    """
    edu_keywords = [
        "b.tech",
        "b.e",
        "bca",
        "mca",
        "bsc",
        "msc",
        "bachelor",
        "master",
        "m.tech",
        "ph.d",
        "degree",
        "university",
        "institute",
        "college"
    ]

    found = []

    for line in text.splitlines():
        lower_line = line.lower()

        if (
            any(keyword in lower_line for keyword in edu_keywords)
            and len(line.strip()) < 120
        ):
            found.append(line.strip())

    return found[:3]


def _estimate_experience(text: str) -> float:
    """
    Estimate years of experience from explicit statements.
    """
    patterns = [
        r"(\d+)(?:\+)?\s+(?:years|yrs)\s+(?:of\s+)?experience",
        r"experience\s*[:\-]?\s*(\d+)(?:\+)?\s*(?:years|yrs)",
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:
            return float(match.group(1))

    return 0.0


def extract_resume_data(pdf_bytes: bytes) -> ResumeData:
    """
    Deterministic PDF -> ResumeData extraction.
    """
    text = extract_text_from_pdf(pdf_bytes)

    return ResumeData(
        name=_extract_name(text),
        email=_extract_email(text),
        phone=_extract_phone(text),
        summary="Profile extracted via deterministic parsing.",
        skills=_extract_skills(text),
        experience_years=_estimate_experience(text),
        job_titles=[],
        certifications=[],
        education=_extract_education(text)
    )