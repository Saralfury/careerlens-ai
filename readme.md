# CareerLens AI
ML-powered career fit analysis system that extracts resume data, scores role alignment, and generates a personalized learning roadmap.

## Demo
[Watch the Demo Video](#) *(Add link here)*

## What it does
- Uploads a resume PDF.
- Extracts structured resume information deterministically (zero LLM dependency).
- Transforms raw text into a rigid feature vector.
- Predicts a role-alignment fit score based on learned patterns from synthetic training data.
- Identifies missing skills.
- Generates a prioritized learning roadmap.

## Why this project
I built CareerLens AI to apply concepts from Python, Pandas, Intro to Machine Learning, and Intermediate Machine Learning to a practical product. It bridges the gap between theoretical coursework and a functional, full-stack data pipeline that demonstrates an end-to-end machine learning workflow using a practical career analysis use case.

## Architecture

```text
Resume PDF
    │
    ▼
PyMuPDF Text Extraction
    │
    ▼
Deterministic Feature Extraction
    │
    ▼
One-Hot Feature Engineering
    │
    ▼
XGBoost Regressor
    │
    ▼
Fit Score + Missing Skills
    │
    ▼
Roadmap Generator
    │
    ▼
React Frontend
(Note: Replace the ASCII art above with ![Architecture Diagram](assets/architecture.png) once you generate your diagram graphic).

Engineering Highlights
Zero external AI/LLM dependencies.

Deterministic resume parsing for reproducible outputs.

End-to-end ML pipeline including training, inference, and deployment.

Synthetic data generation for supervised learning experimentation.

Full-stack architecture using FastAPI and React.

Local inference with pre-trained XGBoost model.

System Flow
User uploads a PDF resume and selects a target role.

The backend deterministically extracts text and structured fields via PyMuPDF.

Extracted skills are mapped into a one-hot encoded feature vector.

The feature vector is passed to a pre-trained XGBoost Regressor.

The model predicts a role-alignment fit score.

Missing skills are identified and converted into a curated learning roadmap.

The React frontend renders the score, matched/missing skills, and the roadmap.

Tech Stack
Backend: Python, FastAPI, PyMuPDF

Machine Learning: XGBoost, Scikit-learn, Pandas, Joblib

Frontend: React, Vite, JavaScript, HTML/CSS

Project Structure
Plaintext
careerlens-ai/
├── backend/
│   ├── main.py
│   ├── extractor.py
│   ├── analyzer.py
│   ├── models.py
│   ├── data.py
│   └── train_model_.py
├── frontend/
│   └── src/
├── start.py
├── xgboost_model.pkl
├── feature_columns.pkl
└── README.md
How It Works
extractor.py: Parses the resume PDF and extracts structured fields using regex and strict keyword matching to ensure zero hallucination.

analyzer.py: Handles fuzzy matching, builds the one-hot encoded feature vector, and runs the XGBoost inference.

data.py: Stores static role definitions, roadmap resources, and generates the synthetic dataset.

train_model_.py: A standalone pipeline that trains the XGBoost Regressor on the synthetic dataset and exports the binary artifacts.

main.py: Exposes the FastAPI endpoints and handles file validation.

App.jsx: Handles the React UI, state management, and API communication.

Model Details
Model used: XGBoost Regressor (xgboost_model.pkl)

Input: A one-hot encoded feature vector representing extracted candidate skills, target role, and continuous experience years.

Output: Predicted Fit Score (0-100).

Training data: 1,500 synthetic candidate profiles generated programmatically to simulate realistic skill distributions and noise.