@echo off
title Income Predictor API

REM Step 1: Activate virtual environment (if any)
REM Uncomment and modify the next line based on your venv path
REM call venv\Scripts\activate.bat

REM Step 2: Start the FastAPI server
start cmd /k "uvicorn app.main:app --reload"

REM Step 3: Open the frontend in the default browser
start "" "frontend\index.html"
