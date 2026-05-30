CAREERLENS AI
================================================================================
ML-powered career fit analysis system that extracts resume data, scores role 
alignment, and generates a personalized learning roadmap.

WHAT IT DOES
--------------------------------------------------------------------------------
* Uploads a resume PDF.
* Extracts structured resume information deterministically (zero LLM dependency).
* Transforms raw text into a rigid feature vector.
* Predicts a role-alignment fit score based on learned patterns from synthetic training data.
* Identifies missing skills.
* Generates a prioritized learning roadmap.

WHY THIS PROJECT
--------------------------------------------------------------------------------
Built to apply concepts from Python, Pandas, Intro to Machine Learning, and 
Intermediate Machine Learning to a practical product. It bridges the gap between 
theoretical coursework and a functional, full-stack data pipeline that demonstrates 
an end-to-end machine learning workflow using a practical career analysis use case.

ARCHITECTURE
--------------------------------------------------------------------------------
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

ENGINEERING HIGHLIGHTS
--------------------------------------------------------------------------------
* Zero external AI/LLM dependencies.
* Deterministic resume parsing for reproducible outputs.
* End-to-end ML pipeline including training, inference, and deployment.
* Synthetic data generation for supervised learning experimentation.
* Full-stack architecture using FastAPI and React.
* Local inference with pre-trained XGBoost model.

SYSTEM FLOW
--------------------------------------------------------------------------------
1. User uploads a PDF resume and selects a target role.
2. The backend deterministically extracts text and structured fields via PyMuPDF.
3. Extracted skills are mapped into a one-hot encoded feature vector.
4. The feature vector is passed to a pre-trained XGBoost Regressor.
5. The model predicts a role-alignment fit score.
6. Missing skills are identified and converted into a curated learning roadmap.
7. The React frontend renders the score, matched/missing skills, and the roadmap.

TECH STACK
--------------------------------------------------------------------------------
* Backend: Python, FastAPI, PyMuPDF
* Machine Learning: XGBoost, Scikit-learn, Pandas, Joblib
* Frontend: React, Vite, JavaScript, HTML/CSS

HOW IT WORKS
--------------------------------------------------------------------------------
* extractor.py: Parses the resume PDF and extracts structured fields using regex 
  and strict keyword matching to ensure zero hallucination.
* analyzer.py: Handles fuzzy matching, builds the one-hot encoded feature vector, 
  and runs the XGBoost inference.
* data.py: Stores static role definitions, roadmap resources, and generates the 
  synthetic dataset.
* train_model_.py: A standalone pipeline that trains the XGBoost Regressor on 
  the synthetic dataset and exports the binary artifacts.
* main.py: Exposes the FastAPI endpoints and handles file validation.
* App.jsx: Handles the React UI, state management, and API communication.

MODEL DETAILS
--------------------------------------------------------------------------------
* Model used: XGBoost Regressor (xgboost_model.pkl)
* Input: A one-hot encoded feature vector representing extracted candidate skills, 
  target role, and continuous experience years.
* Output: Predicted Fit Score (0-100).
* Training data: 1,500 synthetic candidate profiles generated programmatically to 
  simulate realistic skill distributions and noise.

INSTALLATION & SETUP
--------------------------------------------------------------------------------
1. Clone the Repository
   git clone https://github.com/Saralfury/CareerLens-AI.git
   cd CareerLens-AI

2. Backend Setup
   cd backend
   pip install -r requirements.txt

3. Frontend Setup
   cd ../frontend
   npm install
   cd ..

RUN LOCALLY
--------------------------------------------------------------------------------
Boot both the FastAPI backend and the Vite frontend concurrently:

   python start.py

The application will be available at http://localhost:5173.

FUTURE IMPROVEMENTS
--------------------------------------------------------------------------------
* Add better resume parsing capabilities for complex, multi-column layouts.
* Fine-tune model training using real labeled candidate data.
* Expand the static knowledge base with more niche engineering roles.
* Add exportable PDF reports for the generated roadmap.

AUTHOR
--------------------------------------------------------------------------------
* Name: Saral Saini
* GitHub: https://github.com/Saralfury
* Email: sainisaral659@gmail.com