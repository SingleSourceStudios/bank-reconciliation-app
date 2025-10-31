#!/bin/bash

# Kamel Potteries Bank Reconciliation App Runner

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3 to run this application."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install pip3 to run this application."
    exit 1
fi

# Check if required packages are installed
echo "Checking for required packages..."
MISSING_PACKAGES=()
python3 -c "import pandas" 2>/dev/null || MISSING_PACKAGES+=("pandas")
python3 -c "import streamlit" 2>/dev/null || MISSING_PACKAGES+=("streamlit")

if [ ${#MISSING_PACKAGES[@]} -ne 0 ]; then
    echo "Installing missing packages: ${MISSING_PACKAGES[*]}"
    pip3 install "${MISSING_PACKAGES[@]}"
fi

# Run the Streamlit application
echo "Starting Kamel Potteries Bank Reconciliation App..."
echo "Open your web browser to http://localhost:8501"
python3 -m streamlit run app.py