# 🎓 Student Placement Prediction System
### End-to-End ML Deployment on AWS EC2


## 📌 Overview

The **Student Placement Prediction System** is a complete end-to-end Machine Learning deployment project that predicts whether a student is likely to be placed based on academic and aptitude-related parameters. It integrates ML model training, Flask-based web serving, and cloud deployment on **AWS EC2** — demonstrating a real-world **MLOps workflow**.

### Prediction Inputs
| Feature | Description |
|---|---|
| 📊 CGPA | Cumulative Grade Point Average |
| 🧠 IQ | Intelligence Quotient Score |
| 🏅 Profile Score | Co-curricular & extracurricular score |

### Output
> ✅ **Placed** or ❌ **Not Placed** — served via a browser-accessible web interface.

---

## 🏗️ System Architecture

```
Dataset (CSV)
    ↓
Data Preprocessing & EDA
    ↓
Feature Engineering
    ↓
Model Training (Scikit-learn)
    ↓
Model Serialization → student_placement_pipeline_model.pkl
    ↓
Flask Web Application (app.py)
    ↓
AWS EC2 Ubuntu Instance (Port 8000)
    ↓
🌐 Public Web Access
```

---

## 📁 Repository Structure

```
ML-AWS-EC2/
├── ml_model_pipeline.ipynb               # Jupyter notebook: EDA, training, evaluation
├── app.py                                # Flask web app (routes + inference logic)
├── main.py                               # Entry point / demo script
├── student_placement_pipeline_model.pkl  # Serialized trained ML model (18.1 KB)
├── students_placement.csv                # Training dataset (4.1 KB)
├── requirements.txt                      # Pip dependencies
├── pyproject.toml                        # Modern Python project config
├── .python-version                       # Python version pin
├── .gitignore                            # Git exclusion rules
├── uv.lock                               # Dependency lock file (84.4 KB)
└── templates/                            # Flask HTML templates (Jinja2)
    └── index.html                        # Web form + result display
```

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Language | Python 3.12+ |
| ML Libraries | Scikit-learn, Pandas, NumPy, Joblib |
| Web Framework | Flask |
| Cloud Platform | AWS EC2 (Ubuntu Linux) |
| Package Management | UV, pip, venv |
| Serialization | Joblib / Pickle |
| Dev Tools | Jupyter Notebook, Git, PuTTY, WinSCP |

---

## ⚙️ Machine Learning Workflow

### 1. Data Collection
- **Dataset:** `students_placement.csv`
- Features: CGPA, IQ Score, Profile Score, Placement Status

### 2. Exploratory Data Analysis (EDA)
Inside `ml_model_pipeline.ipynb`:
- Statistical inspection & visualization
- Feature correlation & distribution analysis
- Outlier detection & data cleaning

### 3. Preprocessing Pipeline
- Feature scaling with `StandardScaler`
- Train/test split
- Transformation encapsulated within the model pipeline

### 4. Model Training
- Scikit-learn classification algorithm
- Full pipeline: preprocessing → scaling → prediction
- Evaluated on validation set

### 5. Model Serialization
```python
import joblib
joblib.dump(pipeline, "student_placement_pipeline_model.pkl")
```
The serialized model is loaded at runtime — no retraining needed during deployment.

---

## 🌐 Flask Web Application

**File:** `app.py`

### Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Renders the prediction form (HTML UI) |
| `/predict` | POST | Accepts CGPA, IQ, Profile Score → returns placement prediction |

### Inference Flow
```
User Input (Browser Form)
    ↓
POST /predict
    ↓
Input Validation & Conversion
    ↓
Load student_placement_pipeline_model.pkl
    ↓
Model Inference
    ↓
Result → Rendered HTML Response
```

### Running Locally
```bash
python app.py
# Accessible at: http://localhost:8000
```

---

## ☁️ AWS EC2 Deployment

The application is deployed on an **Ubuntu Linux EC2 instance** and publicly accessible via port `8000`.

### Deployment Steps

**1. EC2 Setup**
```
- Launch Ubuntu EC2 instance
- Configure Security Group:
    - SSH (Port 22) — for server access
    - Custom TCP (Port 8000) — for public Flask access
- Generate SSH Key Pair (.pem)
```

**2. Connect via SSH (PuTTY / Terminal)**
```bash
ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
```

**3. Environment Setup on EC2**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**4. Transfer Project Files**
```bash
# Using SCP
scp -i your-key.pem -r ./ML-AWS-EC2 ubuntu@<EC2-PUBLIC-IP>:~/
```

**5. Run the Application**
```bash
python app.py
# Public URL: http://<EC2-PUBLIC-IP>:8000
```

> The app runs with `host="0.0.0.0"` to allow external access.

---

## 🚀 Local Setup & Installation

### Prerequisites
- Python 3.12+
- pip or [uv](https://github.com/astral-sh/uv)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ML-AWS-EC2.git
cd ML-AWS-EC2

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
```

Then open your browser at: `http://localhost:8000`

### Using UV (Recommended)
```bash
uv sync
uv run python app.py
```

---

## 📦 Dependencies

```txt
flask          # Web framework
scikit-learn   # Machine learning
pandas         # Data manipulation
numpy          # Numerical computing
joblib         # Model serialization
```

---

## ✅ MLOps Components

| Component | Status |
|---|---|
| Data Pipeline | ✅ Implemented |
| Model Training | ✅ Implemented |
| Model Serialization | ✅ Implemented |
| Web Serving (Flask) | ✅ Implemented |
| Cloud Deployment (AWS EC2) | ✅ Implemented |
| Environment Management | ✅ Implemented |
| Version Control (Git) | ✅ Implemented |

---

## 🔮 Future Enhancements

- [ ] 🐳 Docker containerization
- [ ] 🔁 CI/CD pipeline (GitHub Actions)
- [ ] 📊 MLflow experiment tracking & model registry
- [ ] 📈 Monitoring & logging
- [ ] ☸️ Kubernetes orchestration
- [ ] 🔄 Automated model retraining
- [ ] 🔒 Nginx + Gunicorn production deployment
- [ ] 🔐 HTTPS / SSL support
- [ ] 📡 REST API versioning

---

## 📚 Educational Value

This project bridges the gap between **notebook experimentation** and **deployable ML systems** by demonstrating:

- Machine Learning lifecycle management
- Backend engineering with Flask
- Linux server administration
- AWS cloud infrastructure setup
- Model serialization and reuse
- Real-world MLOps practices

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> Built with ❤️ to demonstrate real-world ML deployment practices — from training a model to serving it live on the cloud.
