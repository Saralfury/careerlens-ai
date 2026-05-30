ROLE_SKILLS: dict[str, list[str]] = {
    "data scientist": [
        "python", "machine learning", "deep learning", "statistics",
        "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
        "sql", "data visualization", "feature engineering",
        "model evaluation", "jupyter", "matplotlib", "seaborn",
        "hypothesis testing", "regression", "classification", "clustering",
    ],
    "machine learning engineer": [
        "python", "machine learning", "deep learning", "mlops",
        "tensorflow", "pytorch", "scikit-learn", "docker", "kubernetes",
        "api development", "model deployment", "feature engineering",
        "sql", "cloud platforms", "ci/cd", "data pipelines",
        "model monitoring", "a/b testing", "linux", "git",
    ],
    "frontend developer": [
        "html", "css", "javascript", "react", "typescript",
        "responsive design", "rest apis", "git", "webpack", "vite",
        "state management", "testing", "accessibility", "performance optimization",
        "browser devtools", "css frameworks", "component libraries",
        "graphql", "ui/ux principles", "cross-browser compatibility",
    ],
    "backend developer": [
        "python", "node.js", "rest apis", "sql", "postgresql",
        "mongodb", "redis", "docker", "linux", "git",
        "authentication", "authorization", "message queues",
        "microservices", "ci/cd", "api design", "orm",
        "caching", "performance optimization", "testing",
    ],
    "full stack developer": [
        "html", "css", "javascript", "react", "typescript",
        "node.js", "python", "rest apis", "sql", "mongodb",
        "docker", "git", "cloud platforms", "authentication",
        "state management", "responsive design", "testing",
        "ci/cd", "linux", "api design",
    ],
    "devops engineer": [
        "linux", "docker", "kubernetes", "ci/cd", "terraform",
        "ansible", "aws", "azure", "gcp", "bash scripting",
        "monitoring", "logging", "git", "networking",
        "security", "cloud platforms", "infrastructure as code",
        "containerization", "load balancing", "nginx",
    ],
    "data analyst": [
        "sql", "excel", "python", "data visualization", "tableau",
        "power bi", "statistics", "pandas", "numpy",
        "business intelligence", "reporting", "data cleaning",
        "a/b testing", "hypothesis testing", "google analytics",
        "dashboard design", "data storytelling", "etl", "looker", "r",
    ],
    "product manager": [
        "product strategy", "roadmap planning", "user research",
        "agile", "scrum", "data analysis", "stakeholder management",
        "a/b testing", "jira", "confluence", "sql",
        "competitive analysis", "prioritization", "metrics",
        "go-to-market", "ux principles", "customer interviews",
        "okrs", "sprint planning", "product analytics",
    ],
    "cloud architect": [
        "aws", "azure", "gcp", "terraform", "kubernetes",
        "docker", "networking", "security", "microservices",
        "serverless", "cloud storage", "databases", "iam",
        "cost optimization", "high availability", "disaster recovery",
        "ci/cd", "linux", "infrastructure as code", "monitoring",
    ],
    "cybersecurity engineer": [
        "network security", "penetration testing", "vulnerability assessment",
        "firewalls", "siem", "incident response", "python",
        "linux", "cryptography", "threat modeling", "soc",
        "owasp", "cloud security", "identity management",
        "security auditing", "malware analysis", "bash scripting",
        "wireshark", "compliance", "zero trust",
    ],
}

ROADMAP_RESOURCES: dict[str, dict] = {
    "python": {"resources": ["Python.org Official Tutorial", "Automate the Boring Stuff with Python", "Real Python"], "estimated_weeks": 4},
    "machine learning": {"resources": ["Andrew Ng's ML Specialization", "Hands-On ML with Scikit-Learn & TensorFlow", "fast.ai Practical Deep Learning"], "estimated_weeks": 8},
    "deep learning": {"resources": ["Deep Learning Specialization", "PyTorch Official Tutorials", "Dive into Deep Learning"], "estimated_weeks": 10},
    "sql": {"resources": ["SQLZoo", "Mode Analytics SQL Tutorial", "LeetCode SQL Problems"], "estimated_weeks": 3},
    "docker": {"resources": ["Docker Official Get Started Guide", "Play with Docker", "Docker & Kubernetes: The Practical Guide"], "estimated_weeks": 3},
    "kubernetes": {"resources": ["Kubernetes Official Interactive Tutorials", "Kubernetes in Action", "KodeKloud Kubernetes Course"], "estimated_weeks": 5},
    "react": {"resources": ["React Official Docs", "Full Stack Open", "Scrimba React Course"], "estimated_weeks": 5},
    "typescript": {"resources": ["TypeScript Official Handbook", "Execute Program TypeScript Course", "Total TypeScript"], "estimated_weeks": 3},
    "aws": {"resources": ["AWS Cloud Practitioner Essentials", "A Cloud Guru AWS Courses", "AWS Official Documentation"], "estimated_weeks": 6},
    "azure": {"resources": ["Microsoft Learn — Azure Fundamentals Path", "AZ-900 Study Guide", "Azure Portal Free Account"], "estimated_weeks": 5},
    "gcp": {"resources": ["Google Cloud Skills Boost", "Associate Cloud Engineer Prep Course", "GCP Free Tier Hands-on Labs"], "estimated_weeks": 5},
    "tensorflow": {"resources": ["TensorFlow Official Tutorials", "DeepLearning.AI TensorFlow Developer Certificate", "Hands-On ML"], "estimated_weeks": 6},
    "pytorch": {"resources": ["PyTorch Official Tutorials", "fast.ai", "Deep Learning with PyTorch"], "estimated_weeks": 6},
    "statistics": {"resources": ["StatQuest with Josh Starmer", "Think Stats", "Khan Academy Statistics & Probability"], "estimated_weeks": 5},
    "data visualization": {"resources": ["Storytelling with Data", "Matplotlib & Seaborn docs", "Observable"], "estimated_weeks": 3},
    "git": {"resources": ["Pro Git Book", "GitHub Skills", "Oh My Git!"], "estimated_weeks": 2},
    "linux": {"resources": ["Linux Command Line", "OverTheWire: Bandit wargame", "The Odin Project"], "estimated_weeks": 3},
    "terraform": {"resources": ["HashiCorp Learn", "Terraform: Up & Running", "KodeKloud Terraform Course"], "estimated_weeks": 4},
    "ci/cd": {"resources": ["GitHub Actions Official Docs", "GitLab CI/CD Documentation", "The DevOps Handbook"], "estimated_weeks": 3},
    "javascript": {"resources": ["javascript.info", "Eloquent JavaScript", "freeCodeCamp JavaScript"], "estimated_weeks": 6},
    "html": {"resources": ["MDN Web Docs", "The Odin Project", "freeCodeCamp Responsive Web Design"], "estimated_weeks": 2},
    "css": {"resources": ["MDN Web Docs", "CSS Tricks", "Kevin Powell YouTube Channel"], "estimated_weeks": 3},
    "rest apis": {"resources": ["REST API Design Best Practices", "FastAPI Official Tutorial", "Postman Learning Center"], "estimated_weeks": 3},
    "node.js": {"resources": ["Node.js Official Docs", "The Odin Project", "Node.js Design Patterns"], "estimated_weeks": 5},
    "mlops": {"resources": ["MLOps Specialization", "Made With ML", "Full Stack Deep Learning"], "estimated_weeks": 7},
    "scikit-learn": {"resources": ["Scikit-learn Official User Guide", "ML with Python Cookbook", "Kaggle Intro to Machine Learning"], "estimated_weeks": 4},
    "pandas": {"resources": ["Pandas Official Documentation", "Kaggle Pandas Course", "Python for Data Analysis"], "estimated_weeks": 3},
    "numpy": {"resources": ["NumPy Official Documentation", "NumPy Illustrated", "Kaggle NumPy exercises"], "estimated_weeks": 2},
    "agile": {"resources": ["Scrum Guide", "Mountain Goat Software", "Agile Manifesto and Principles"], "estimated_weeks": 2},
    "penetration testing": {"resources": ["TryHackMe", "HackTheBox Academy", "The Web Application Hacker's Handbook"], "estimated_weeks": 10},
    "network security": {"resources": ["Professor Messer CompTIA Security+", "Cybrary Network Security Fundamentals", "NIST Cybersecurity Framework"], "estimated_weeks": 6},
    "tableau": {"resources": ["Tableau Public Free Training Videos", "Tableau Official eLearning", "Tableau Desktop Specialist Prep"], "estimated_weeks": 4},
    "power bi": {"resources": ["Microsoft Learn — Power BI Path", "Guy in a Cube", "Power BI Guided Learning"], "estimated_weeks": 3},
    "mongodb": {"resources": ["MongoDB University", "MongoDB Official Documentation", "The Definitive Guide to MongoDB"], "estimated_weeks": 3},
    "redis": {"resources": ["Redis University", "Redis Official Documentation", "Redis in Action"], "estimated_weeks": 2},
    "postgresql": {"resources": ["PostgreSQL Official Tutorial", "PgExercises", "The Art of PostgreSQL"], "estimated_weeks": 4},
    "feature engineering": {"resources": ["Feature Engineering for ML", "Kaggle Feature Engineering Course", "Featuretools Documentation"], "estimated_weeks": 3},
    "model deployment": {"resources": ["FastAPI for ML APIs", "BentoML Official Documentation", "Full Stack Deep Learning"], "estimated_weeks": 4},
    "cloud platforms": {"resources": ["AWS Free Tier", "Google Cloud Free Program", "Microsoft Azure Free Account"], "estimated_weeks": 5},
    "testing": {"resources": ["pytest Official Documentation", "Jest Official Documentation", "Test-Driven Development with Python"], "estimated_weeks": 3},
    "responsive design": {"resources": ["MDN — Responsive Design Guide", "CSS Tricks — A Guide to Flexbox", "web.dev — Responsive Design"], "estimated_weeks": 2},
    "state management": {"resources": ["React Context & useReducer", "Zustand Official Docs", "Redux Toolkit Quick Start"], "estimated_weeks": 2},
}

DEFAULT_RESOURCE = {
    "resources": [
        "Search for official documentation",
        "Look for a relevant Coursera or Udemy course",
        "Practice on relevant project or Kaggle challenge",
    ],
    "estimated_weeks": 4,
}
import random
import pandas as pd

def generate_training_data(num_samples: int = 1500) -> tuple[pd.DataFrame, list[str]]:
    """Generates synthetic resume data to train the XGBoost model."""
    all_skills = sorted(list({skill for skills in ROLE_SKILLS.values() for skill in skills}))
    roles = list(ROLE_SKILLS.keys())

    data = []
    for _ in range(num_samples):
        role = random.choice(roles)
        req_skills = ROLE_SKILLS[role]
        
        exp_years = round(random.uniform(0, 10), 1)
        
        candidate_skills = set()
        for s in req_skills:
            if random.random() > 0.3:  # 70% chance to have a required skill
                candidate_skills.add(s)
        for s in all_skills:
            if random.random() > 0.9:  # 10% chance to have an irrelevant skill
                candidate_skills.add(s)
                
        # Generate baseline target score with synthetic noise
        matched = len(candidate_skills.intersection(set(req_skills)))
        skill_score = (matched / len(req_skills)) * 70 if req_skills else 0
        exp_bonus = min(30, (exp_years / 8) * 30)
        noise = random.uniform(-5, 5)
        fit_score = max(0, min(100, round(skill_score + exp_bonus + noise)))
        
        # Build feature vector
        row = {"target_role": role, "experience_years": exp_years}
        for s in all_skills:
            row[s] = 1 if s in candidate_skills else 0
        row["fit_score"] = fit_score
        
        data.append(row)
        
    return pd.DataFrame(data), all_skills