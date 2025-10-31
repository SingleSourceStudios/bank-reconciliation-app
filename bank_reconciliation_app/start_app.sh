#!/bin/bash

# Kamel Potteries Bank Reconciliation App Starter

echo "🚀 Starting Kamel Potteries Bank Reconciliation App..."
echo "=============================================="

# Check if required packages are installed
echo "Checking for required packages..."
if python3 -c "import streamlit" 2>/dev/null; then
    echo "✅ Streamlit is installed"
else
    echo "❌ Streamlit not found. Installing..."
    pip install streamlit
fi

if python3 -c "import pandas" 2>/dev/null; then
    echo "✅ Pandas is installed"
else
    echo "❌ Pandas not found. Installing..."
    pip install pandas
fi

# Start the application
echo ""
echo "Starting the application on http://localhost:8503"
echo "Press Ctrl+C to stop the application"
echo ""

cd /Users/rain-c/Documents/kamel-app/bank_reconciliation_app
python3 -m streamlit run app.py --server.headless true --server.port 8503 --server.address localhost