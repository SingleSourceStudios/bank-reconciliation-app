"""
Data processing modules for bank statements and Xero data
"""
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Any, Optional

class BankStatementProcessor:
    """Process bank statement data"""
    
    def __init__(self):
        self.data = None
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load bank statement data from CSV file
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Processed bank statement data
        """
        try:
            # Try different separators and encodings
            separators = [';', ',', '\t']
            df = None
            
            for sep in separators:
                try:
                    # Try reading with the current separator
                    temp_df = pd.read_csv(file_path, sep=sep, dtype=str, on_bad_lines='skip')
                    if len(temp_df.columns) >= 2:  # At least date and amount columns
                        df = temp_df
                        break
                except Exception:
                    continue
            
            if df is None:
                # Fallback: try reading without specifying separator
                df = pd.read_csv(file_path, dtype=str, on_bad_lines='skip')
            
            # Clean column names (remove asterisks and extra spaces)
            df.columns = [col.replace('*', '').strip() for col in df.columns]
            
            # Identify date and amount columns
            date_col = self._find_date_column(df)
            amount_col = self._find_amount_column(df)
            
            if date_col is None or amount_col is None:
                raise Exception("Could not identify required Date and Amount columns")
            
            # Rename columns to expected names
            column_mapping = {
                date_col: 'Date',
                amount_col: 'Amount'
            }
            
            # Try to find other useful columns
            payee_col = self._find_payee_column(df)
            description_col = self._find_description_column(df)
            reference_col = self._find_reference_column(df)
            
            if payee_col:
                column_mapping[payee_col] = 'Payee'
            if description_col:
                column_mapping[description_col] = 'Description'
            if reference_col:
                column_mapping[reference_col] = 'Reference'
            
            df = df.rename(columns=column_mapping)
            
            # Convert date column to datetime
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            
            # Convert amount to numeric
            df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
            
            # Show info about data processing
            initial_count = len(df)
            
            # Drop rows with invalid dates
            df = df.dropna(subset=['Date'])
            
            # Show info about dropped rows
            if initial_count > len(df):
                print(f"Dropped {initial_count - len(df)} rows due to invalid dates")
            
            # Convert invalid amounts to 0 instead of dropping them
            invalid_amounts = df['Amount'].isna().sum()
            if invalid_amounts > 0:
                print(f"Found {invalid_amounts} rows with invalid amounts, setting to 0")
            df['Amount'] = df['Amount'].fillna(0)
            
            # Sort by date
            df = df.sort_values('Date').reset_index(drop=True)
            
            self.data = df
            return self.data
            
        except Exception as e:
            raise Exception(f"Error loading bank statement data: {str(e)}")
    
    def _find_date_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the date column in the dataframe"""
        date_keywords = ['date', 'datum']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in date_keywords):
                return col
        # If no keyword match, return the first column
        return df.columns[0] if len(df.columns) > 0 else None
    
    def _find_amount_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the amount column in the dataframe"""
        amount_keywords = ['amount', 'spent', 'received', 'debit', 'credit']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in amount_keywords):
                return col
        # If no keyword match, return the second column (common convention)
        return df.columns[1] if len(df.columns) > 1 else None
    
    def _find_payee_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the payee column in the dataframe"""
        payee_keywords = ['payee', 'recipient', 'to', 'from']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in payee_keywords):
                return col
        return None
    
    def _find_description_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the description column in the dataframe"""
        description_keywords = ['description', 'desc', 'details', 'memo']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in description_keywords):
                return col
        return None
    
    def _find_reference_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the reference column in the dataframe"""
        reference_keywords = ['reference', 'ref', 'transaction']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in reference_keywords):
                return col
        return None
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Get summary statistics for bank statement data"""
        if self.data is None:
            raise Exception("No data loaded. Please load data first.")
        
        return {
            "total_transactions": len(self.data),
            "date_range": {
                "start": self.data['Date'].min(),
                "end": self.data['Date'].max()
            },
            "total_debits": self.data[self.data['Amount'] < 0]['Amount'].sum(),
            "total_credits": self.data[self.data['Amount'] > 0]['Amount'].sum(),
            "net_change": self.data['Amount'].sum()
        }

class XeroDataProcessor:
    """Process Xero accounting data"""
    
    def __init__(self):
        self.data = None
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load Xero data from CSV file
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Processed Xero data
        """
        try:
            # Try different separators and encodings
            separators = [',', ';', '\t']
            df = None
            
            for sep in separators:
                try:
                    # Try reading with the current separator
                    temp_df = pd.read_csv(file_path, sep=sep, dtype=str, on_bad_lines='skip')
                    if len(temp_df.columns) >= 2:  # At least date and amount columns
                        df = temp_df
                        break
                except Exception:
                    continue
            
            if df is None:
                # Fallback: try reading without specifying separator
                df = pd.read_csv(file_path, dtype=str, on_bad_lines='skip')
            
            # Clean column names (remove asterisks and extra spaces)
            df.columns = [col.replace('*', '').strip() for col in df.columns]
            
            # Identify date and amount columns
            date_col = self._find_date_column(df)
            amount_col = self._find_amount_column(df)
            
            if date_col is None or amount_col is None:
                raise Exception("Could not identify required Date and Amount columns")
            
            # Rename columns to expected names
            column_mapping = {
                date_col: 'Date',
                amount_col: 'Amount'
            }
            
            # Try to find other useful columns
            description_col = self._find_description_column(df)
            reference_col = self._find_reference_column(df)
            
            if description_col:
                column_mapping[description_col] = 'Description'
            if reference_col:
                column_mapping[reference_col] = 'Reference'
            
            df = df.rename(columns=column_mapping)
            
            # Convert date column to datetime
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            
            # For Xero data, we need to handle spent/received columns
            # If we have separate spent and received columns, combine them
            if 'Spent' in df.columns and 'Received' in df.columns:
                # Convert to numeric
                df['Spent'] = pd.to_numeric(df['Spent'], errors='coerce').fillna(0)
                df['Received'] = pd.to_numeric(df['Received'], errors='coerce').fillna(0)
                # Combine into a single Amount column (Received - Spent)
                df['Amount'] = df['Received'] - df['Spent']
            else:
                # Convert amount to numeric
                df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
            
            # Show info about data processing
            initial_count = len(df)
            
            # Drop rows with invalid dates
            df = df.dropna(subset=['Date'])
            
            # Show info about dropped rows
            if initial_count > len(df):
                print(f"Dropped {initial_count - len(df)} rows due to invalid dates")
            
            # Convert invalid amounts to 0 instead of dropping them
            invalid_amounts = df['Amount'].isna().sum()
            if invalid_amounts > 0:
                print(f"Found {invalid_amounts} rows with invalid amounts, setting to 0")
            df['Amount'] = df['Amount'].fillna(0)
            
            # Sort by date
            df = df.sort_values('Date').reset_index(drop=True)
            
            self.data = df
            return self.data
            
        except Exception as e:
            raise Exception(f"Error loading Xero data: {str(e)}")
    
    def _find_date_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the date column in the dataframe"""
        date_keywords = ['date', 'datum']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in date_keywords):
                return col
        # If no keyword match, return the first column
        return df.columns[0] if len(df.columns) > 0 else None
    
    def _find_amount_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the amount column in the dataframe"""
        amount_keywords = ['amount', 'spent', 'received', 'debit', 'credit']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in amount_keywords):
                return col
        # If no keyword match, return the second column (common convention)
        return df.columns[1] if len(df.columns) > 1 else None
    
    def _find_description_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the description column in the dataframe"""
        description_keywords = ['description', 'desc', 'details', 'memo']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in description_keywords):
                return col
        return None
    
    def _find_reference_column(self, df: pd.DataFrame) -> Optional[str]:
        """Find the reference column in the dataframe"""
        reference_keywords = ['reference', 'ref', 'transaction']
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in reference_keywords):
                return col
        return None
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Get summary statistics for Xero data"""
        if self.data is None:
            raise Exception("No data loaded. Please load data first.")
        
        return {
            "total_transactions": len(self.data),
            "date_range": {
                "start": self.data['Date'].min(),
                "end": self.data['Date'].max()
            },
            "total_debits": self.data[self.data['Amount'] < 0]['Amount'].sum(),
            "total_credits": self.data[self.data['Amount'] > 0]['Amount'].sum(),
            "net_change": self.data['Amount'].sum()
        }