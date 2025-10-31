"""
Configuration file for Kamel Potteries Bank Reconciliation App
"""
import os

class Config:
    # Default tolerance settings
    DEFAULT_TOLERANCE_DAYS = 3
    DEFAULT_TOLERANCE_AMOUNT = 0.01
    
    # File paths
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    UPLOADS_DIR = os.path.join(DATA_DIR, "uploads")
    SAMPLE_DATA_DIR = os.path.join(DATA_DIR, "sample_data")
    
    # Output settings
    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
    
    # Date format for bank statements
    BANK_DATE_FORMAT = "%d/%m/%Y"
    
    # Date format for Xero data
    XERO_DATE_FORMAT = "%Y-%m-%d"
    
    # Column mappings
    BANK_COLUMNS = {
        'date': 'Date',
        'amount': 'Amount',
        'payee': 'Payee',
        'description': 'Description',
        'reference': 'Reference',
        'check_number': 'Check Number'
    }
    
    XERO_COLUMNS = {
        'date': 'Date',
        'amount': 'Amount',
        'payee': 'Payee',
        'description': 'Description',
        'reference': 'Reference',
        'check_number': 'Check Number'
    }

# Create directories if they don't exist
os.makedirs(Config.UPLOADS_DIR, exist_ok=True)
os.makedirs(Config.OUTPUT_DIR, exist_ok=True)