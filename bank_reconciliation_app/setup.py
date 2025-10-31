"""
Setup script for Kamel Potteries Bank Reconciliation App
"""
from setuptools import setup, find_packages

setup(
    name="kamel-bank-reconciliation",
    version="1.0.0",
    description="Bank statement reconciliation tool for Kamel Potteries",
    author="Kamel Potteries Finance Team",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "streamlit>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "bank-reconcile=bank_reconciliation_app.app:main",
        ],
    },
    python_requires=">=3.7",
)