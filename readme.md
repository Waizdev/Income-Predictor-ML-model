# 💰 Income Predictor - Machine Learning Web App

This is a locally deployed machine learning application that predicts whether an individual earns **more than $50K** based on demographic and work-related inputs.

🚀 Powered by **FastAPI (Backend)** and a custom-built **HTML/CSS/JavaScript UI (Frontend)**.

---

## 📌 Project Overview

This project combines **Exploratory Data Analysis (EDA)** and a **Random Forest Classifier** trained on the `adult.csv` dataset. It features:

- Clean UI with form-based input
- Live ML model predictions
- Confidence score feedback
- Easy local deployment with `.bat` launcher

---

## 🧠 Model Information

- **Algorithm:** Random Forest Classifier  
- **Dataset:** [Adult Income Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/adult)
- **Features Used:**
  - Age
  - Education Number
  - Hours Worked Per Week
  - Capital Gain/Loss
  - Workclass (Private)
  - Marital Status
  - Occupation (Exec-managerial)
  - Sex
  - Native Country (US)


---

## ⚙️ Requirements

Install dependencies:

pip install -r requirements.txt

Contents of requirements.txt:


fastapi

uvicorn

joblib

scikit-learn

python-multipart

jinja2

numpy

▶️ How to Run

Clone the repo or download it

Install the dependencies

Double-click run.bat

– This will start the API server and open the UI

Or run manually:

uvicorn app.main:app --reload

🤝 Credits

Developed by Syed Muhammad Waiz Rizvi

Bachelor’s in Artificial Intelligence | 4th Semester

University of Management and Technology, Lahore

📫 Contact

Want to collaborate or improve this app? Open an issue or connect with me!
---



