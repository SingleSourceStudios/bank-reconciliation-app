@echo off
title Kamel Potteries Bank Reconciliation App

echo 🚀 Starting Kamel Potteries Bank Reconciliation App...
echo ==============================================

REM Check if required packages are installed
echo Checking for required packages...
python -c "import streamlit" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Streamlit not found. Installing...
    pip install streamlit
) else (
    echo ✅ Streamlit is installed
)

python -c "import pandas" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Pandas not found. Installing...
    pip install pandas
) else (
    echo ✅ Pandas is installed
)

REM Start the application
echo.
echo Starting the application on http://localhost:8503
echo Press Ctrl+C to stop the application
echo.

cd /d "%~dp0"
python -m streamlit run app.py --server.headless true --server.port 8503 --server.address localhost

pause