from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load trained model
model = joblib.load("app/model/income_model.pkl")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    age: int = Form(...),
    education_num: int = Form(...),
    hours_per_week: int = Form(...),
    capital_gain: int = Form(...),
    capital_loss: int = Form(...),
    is_private: int = Form(...),
    is_married: int = Form(...),
    is_exec: int = Form(...),
    is_male: int = Form(...),
    is_us: int = Form(...)
):
    # Match feature order used during training
    input_data = np.array([[age, education_num, capital_gain, capital_loss, hours_per_week,
                            is_private, is_married, is_exec, is_male, is_us]])
    
    pred = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][pred] * 100

    label = "🟢 High Earner (>50K)" if pred == 1 else "🔴 Low Earner (<=50K)"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction_text": f"💡 Prediction Result: {label}",
        "confidence": f"📊 Model Confidence: {proba:.2f}%"
    })
