"""
Utility functions for Kamel Potteries Bank Reconciliation App
"""
import os
import pandas as pd
from typing import List, Dict, Any

def format_currency(amount: float) -> str:
    """Format amount as currency string"""
    return f"R{amount:,.2f}"

def format_date(date_obj) -> str:
    """Format date object as string"""
    if hasattr(date_obj, 'strftime'):
        return date_obj.strftime('%Y-%m-%d')
    return str(date_obj)

def validate_csv_file(file_path: str) -> bool:
    """Validate if file is a valid CSV"""
    try:
        pd.read_csv(file_path, nrows=1)
        return True
    except Exception:
        return False

def get_file_info(file_path: str) -> Dict[str, Any]:
    """Get information about a file"""
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    
    stat = os.stat(file_path)
    return {
        "size": stat.st_size,
        "modified": stat.st_mtime,
        "is_file": os.path.isfile(file_path),
        "is_directory": os.path.isdir(file_path)
    }

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to remove invalid characters"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def find_csv_files(directory: str) -> List[str]:
    """Find all CSV files in a directory"""
    csv_files = []
    if os.path.exists(directory) and os.path.isdir(directory):
        for file in os.listdir(directory):
            if file.lower().endswith('.csv'):
                csv_files.append(os.path.join(directory, file))
    return csv_files

def compare_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare two dataframes and return differences"""
    comparison = {
        "rows_df1": len(df1),
        "rows_df2": len(df2),
        "columns_df1": list(df1.columns),
        "columns_df2": list(df2.columns),
        "common_columns": list(set(df1.columns) & set(df2.columns))
    }
    
    return comparison