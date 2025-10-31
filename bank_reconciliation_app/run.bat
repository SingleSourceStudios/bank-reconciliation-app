@echo off
title Kamel Potteries Bank Reconciliation App

echo Kamel Potteries Bank Reconciliation App
echo ======================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3 and make sure it's in your PATH.
    pause
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed.
    echo Please install pip to run this application.
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking for required packages...
python -c "import pandas" 2>nul
if %errorlevel% neq 0 (
    echo Installing pandas...
    pip install pandas
)

python -c "import streamlit" 2>nul
if %errorlevel% neq 0 (
    echo Installing streamlit...
    pip install streamlit
)

REM Run the Streamlit application
echo Starting Kamel Potteries Bank Reconciliation App...
echo Open your web browser to http://localhost:8501
python -m streamlit run app.py

pause