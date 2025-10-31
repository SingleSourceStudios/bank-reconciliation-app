"""
Reconciliation engine to match bank statements with Xero data
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple

class ReconciliationEngine:
    """Engine to reconcile bank statements with Xero data"""
    
    def __init__(self, tolerance_days: int = 3, tolerance_amount: float = 0.01):
        """
        Initialize reconciliation engine
        
        Args:
            tolerance_days (int): Number of days to consider for date matching
            tolerance_amount (float): Amount tolerance for matching transactions
        """
        self.tolerance_days = tolerance_days
        self.tolerance_amount = tolerance_amount
    
    def find_discrepancies(self, bank_data: pd.DataFrame, xero_data: pd.DataFrame) -> List[Dict[str, Any]]:
        """
        Find discrepancies between bank statement and Xero data
        
        Args:
            bank_data (pd.DataFrame): Bank statement data
            xero_data (pd.DataFrame): Xero accounting data
            
        Returns:
            List[Dict[str, Any]]: List of discrepancies found
        """
        discrepancies = []
        
        # Create copies to avoid modifying original data
        bank_df = bank_data.copy()
        xero_df = xero_data.copy()
        
        # Add matched flags
        bank_df['matched'] = False
        xero_df['matched'] = False
        
        # Match transactions based on date and amount
        matched_pairs = self._match_transactions(bank_df, xero_df)
        
        # Mark matched transactions
        for bank_idx, xero_idx in matched_pairs:
            bank_df.loc[bank_idx, 'matched'] = True
            xero_df.loc[xero_idx, 'matched'] = True
        
        # Find unmatched bank transactions
        unmatched_bank = bank_df[bank_df['matched'] == False]
        for _, row in unmatched_bank.iterrows():
            discrepancies.append({
                'type': 'unmatched_bank',
                'date': row['Date'],
                'amount': row['Amount'],
                'description': row.get('Description', ''),
                'reference': row.get('Reference', ''),
                'payee': row.get('Payee', ''),
                'details': 'Transaction found in bank statement but not in Xero'
            })
        
        # Find unmatched Xero transactions
        unmatched_xero = xero_df[xero_df['matched'] == False]
        for _, row in unmatched_xero.iterrows():
            discrepancies.append({
                'type': 'unmatched_xero',
                'date': row['Date'],
                'amount': row['Amount'],
                'description': row.get('Description', ''),
                'reference': row.get('Reference', ''),
                'payee': row.get('Payee', ''),
                'details': 'Transaction found in Xero but not in bank statement'
            })
        
        # Find potential duplicates (same amount, similar dates)
        duplicates = self._find_duplicates(bank_df, xero_df)
        discrepancies.extend(duplicates)
        
        return discrepancies
    
    def _match_transactions(self, bank_df: pd.DataFrame, xero_df: pd.DataFrame) -> List[Tuple[int, int]]:
        """
        Match transactions based on date and amount
        
        Args:
            bank_df (pd.DataFrame): Bank statement data with matched column
            xero_df (pd.DataFrame): Xero data with matched column
            
        Returns:
            List[Tuple[int, int]]: List of matched index pairs (bank_idx, xero_idx)
        """
        matches = []
        
        # Get unmatched transactions
        unmatched_bank = bank_df[bank_df['matched'] == False]
        unmatched_xero = xero_df[xero_df['matched'] == False]
        
        for bank_idx, bank_row in unmatched_bank.iterrows():
            bank_date = bank_row['Date']
            bank_amount = bank_row['Amount']
            
            # Look for matching Xero transaction
            for xero_idx, xero_row in unmatched_xero.iterrows():
                if xero_df.loc[xero_idx, 'matched']:
                    continue
                    
                xero_date = xero_row['Date']
                xero_amount = xero_row['Amount']
                
                # Check if dates are within tolerance
                date_diff = abs((bank_date - xero_date).days)
                if date_diff > self.tolerance_days:
                    continue
                
                # Check if amounts match within tolerance
                if abs(bank_amount - xero_amount) <= self.tolerance_amount:
                    matches.append((bank_idx, xero_idx))
                    break
        
        return matches
    
    def _find_duplicates(self, bank_df: pd.DataFrame, xero_df: pd.DataFrame) -> List[Dict[str, Any]]:
        """
        Find potential duplicate transactions
        
        Args:
            bank_df (pd.DataFrame): Bank statement data
            xero_df (pd.DataFrame): Xero data
            
        Returns:
            List[Dict[str, Any]]: List of potential duplicates
        """
        duplicates = []
        
        # Check for duplicates within bank statements
        bank_duplicates = bank_df[bank_df.duplicated(subset=['Date', 'Amount'], keep=False)]
        for _, row in bank_duplicates.iterrows():
            duplicates.append({
                'type': 'duplicate_bank',
                'date': row['Date'],
                'amount': row['Amount'],
                'description': row.get('Description', ''),
                'reference': row.get('Reference', ''),
                'payee': row.get('Payee', ''),
                'details': 'Potential duplicate transaction in bank statement'
            })
        
        # Check for duplicates within Xero data
        xero_duplicates = xero_df[xero_df.duplicated(subset=['Date', 'Amount'], keep=False)]
        for _, row in xero_duplicates.iterrows():
            duplicates.append({
                'type': 'duplicate_xero',
                'date': row['Date'],
                'amount': row['Amount'],
                'description': row.get('Description', ''),
                'reference': row.get('Reference', ''),
                'payee': row.get('Payee', ''),
                'details': 'Potential duplicate transaction in Xero data'
            })
        
        return duplicates