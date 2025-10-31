"""
PDF Processor for Bank Reconciliation App
Handles conversion of PDF bank statements and Xero reports to CSV format
"""
import PyPDF2
import pdfplumber
import pandas as pd
import csv
import re
import os
from io import StringIO
from typing import List, Dict, Any

class PDFProcessor:
    """Process PDF files and extract tabular data"""
    
    def __init__(self):
        pass
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extract text from PDF file
        
        Args:
            pdf_path (str): Path to PDF file
            
        Returns:
            str: Extracted text
        """
        text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            # Fallback to PyPDF2 if pdfplumber fails
            try:
                with open(pdf_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
            except Exception as e2:
                raise Exception(f"Failed to extract text from PDF: {str(e2)}")
        
        return text
    
    def extract_tables_from_pdf(self, pdf_path: str) -> List[List[List[str]]]:
        """
        Extract tables from PDF file
        
        Args:
            pdf_path (str): Path to PDF file
            
        Returns:
            List[List[List[str]]]: List of tables, each table is a list of rows, each row is a list of cells
        """
        tables = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_tables = page.extract_tables()
                    if page_tables:
                        tables.extend(page_tables)
        except Exception as e:
            print(f"Warning: Could not extract tables with pdfplumber: {e}")
            # Return empty list if table extraction fails
            tables = []
        
        return tables
    
    def process_bank_statement_pdf(self, pdf_path: str, csv_path: str) -> bool:
        """
        Process bank statement PDF and convert to proper CSV format
        
        Args:
            pdf_path (str): Path to bank statement PDF
            csv_path (str): Path to output CSV file
            
        Returns:
            bool: True if conversion successful, False otherwise
        """
        try:
            # Try to extract tables first
            tables = self.extract_tables_from_pdf(pdf_path)
            
            if tables:
                # Look for transaction tables
                transaction_data = []
                
                for table in tables:
                    # Look for tables that contain transaction data
                    for row in table:
                        # Check if this looks like a transaction row
                        if self._is_transaction_row(row):
                            transaction_data.append(row)
                
                if transaction_data:
                    # Write to CSV with proper headers
                    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile, delimiter=';')
                        # Write header
                        writer.writerow(['*Date', '*Amount', 'Payee', 'Description', 'Reference', 'Check Number'])
                        # Write transaction data
                        for row in transaction_data:
                            writer.writerow(row[:6])  # Limit to 6 columns
                    return True
            
            # If no tables found, try text extraction and parsing
            text = self.extract_text_from_pdf(pdf_path)
            transactions = self._parse_bank_statement_text(text)
            
            if transactions:
                with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';')
                    # Write header
                    writer.writerow(['*Date', '*Amount', 'Payee', 'Description', 'Reference', 'Check Number'])
                    # Write transactions
                    for transaction in transactions:
                        writer.writerow([
                            transaction.get('date', ''),
                            transaction.get('amount', ''),
                            transaction.get('payee', ''),
                            transaction.get('description', ''),
                            transaction.get('reference', ''),
                            transaction.get('check_number', '')
                        ])
                return True
            
            return False
            
        except Exception as e:
            print(f"Error processing bank statement PDF: {e}")
            return False
    
    def process_xero_pdf(self, pdf_path: str, csv_path: str) -> bool:
        """
        Process Xero PDF and convert to proper CSV format
        
        Args:
            pdf_path (str): Path to Xero PDF
            csv_path (str): Path to output CSV file
            
        Returns:
            bool: True if conversion successful, False otherwise
        """
        try:
            # Try to extract tables first
            tables = self.extract_tables_from_pdf(pdf_path)
            
            if tables:
                # Look for transaction tables
                transaction_data = []
                headers = None
                
                for table in tables:
                    if table:
                        # Use first row as headers if it looks like headers
                        if self._looks_like_headers(table[0]):
                            headers = table[0]
                            # Add remaining rows as data
                            for row in table[1:]:
                                transaction_data.append(row)
                        else:
                            # Add all rows as data
                            transaction_data.extend(table)
                
                if transaction_data:
                    # Write to CSV
                    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        # Write headers if we found them
                        if headers:
                            # Map Xero headers to our expected format
                            mapped_headers = self._map_xero_headers(headers)
                            writer.writerow(mapped_headers)
                        else:
                            # Use default headers
                            writer.writerow(['Date', 'Description', 'Reference', 'Payment Ref', 'Spent', 'Received'])
                        
                        # Write transaction data
                        for row in transaction_data:
                            # Process row to match expected format
                            processed_row = self._process_xero_row(row)
                            writer.writerow(processed_row)
                    return True
            
            # If no tables found, try text extraction
            text = self.extract_text_from_pdf(pdf_path)
            transactions = self._parse_xero_text(text)
            
            if transactions:
                with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Date', 'Description', 'Reference', 'Payment Ref', 'Spent', 'Received'])
                    for transaction in transactions:
                        writer.writerow([
                            transaction.get('date', ''),
                            transaction.get('description', ''),
                            transaction.get('reference', ''),
                            transaction.get('payment_ref', ''),
                            transaction.get('spent', ''),
                            transaction.get('received', '')
                        ])
                return True
            
            return False
            
        except Exception as e:
            print(f"Error processing Xero PDF: {e}")
            return False
    
    def _is_transaction_row(self, row: List[str]) -> bool:
        """
        Check if a row looks like a transaction row
        
        Args:
            row (List[str]): Row data
            
        Returns:
            bool: True if row looks like transaction data
        """
        if len(row) < 3:
            return False
        
        # Check if first element looks like a date
        date_pattern = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
        if re.match(date_pattern, str(row[0])):
            # Check if second element looks like an amount
            amount_pattern = r'[+-]?\d+([.,]\d+)?'
            if re.match(amount_pattern, str(row[1]).replace(' ', '')):
                return True
        
        return False
    
    def _looks_like_headers(self, row: List[str]) -> bool:
        """
        Check if a row looks like headers
        
        Args:
            row (List[str]): Row data
            
        Returns:
            bool: True if row looks like headers
        """
        header_keywords = ['date', 'description', 'reference', 'amount', 'spent', 'received', 'payment']
        row_str = ' '.join(str(cell).lower() for cell in row)
        return any(keyword in row_str for keyword in header_keywords)
    
    def _map_xero_headers(self, headers: List[str]) -> List[str]:
        """
        Map Xero headers to our expected format
        
        Args:
            headers (List[str]): Original headers
            
        Returns:
            List[str]: Mapped headers
        """
        # Simple mapping for now
        return ['Date', 'Description', 'Reference', 'Payment Ref', 'Spent', 'Received']
    
    def _process_xero_row(self, row: List[str]) -> List[str]:
        """
        Process a Xero data row
        
        Args:
            row (List[str]): Original row
            
        Returns:
            List[str]: Processed row
        """
        # For now, just return the row as is
        return row
    
    def _parse_bank_statement_text(self, text: str) -> List[Dict[str, str]]:
        """
        Parse bank statement text to extract transactions
        
        Args:
            text (str): Bank statement text
            
        Returns:
            List[Dict[str, str]]: List of transactions
        """
        transactions = []
        lines = text.split('\n')
        
        # Look for transaction patterns
        transaction_pattern = r'(\d{1,2}/\d{1,2}/\d{4})\s+(.+?)\s+([+-]?\d+(?:[.,]\d+)?)'
        
        for line in lines:
            match = re.search(transaction_pattern, line)
            if match:
                transactions.append({
                    'date': match.group(1),
                    'description': match.group(2).strip(),
                    'amount': match.group(3)
                })
        
        return transactions
    
    def _parse_xero_text(self, text: str) -> List[Dict[str, str]]:
        """
        Parse Xero text to extract transactions
        
        Args:
            text (str): Xero text
            
        Returns:
            List[Dict[str, str]]: List of transactions
        """
        transactions = []
        lines = text.split('\n')
        
        # Look for transaction patterns
        transaction_pattern = r'(\d{1,2} \w{3} \d{4})\s+(.+?)\s+([+-]?\d+(?:[.,]\d+)?)'
        
        for line in lines:
            match = re.search(transaction_pattern, line)
            if match:
                transactions.append({
                    'date': match.group(1),
                    'description': match.group(2).strip(),
                    'amount': match.group(3)
                })
        
        return transactions
    
    def pdf_to_csv(self, pdf_path: str, csv_path: str) -> bool:
        """
        Convert PDF to CSV format
        
        Args:
            pdf_path (str): Path to input PDF file
            csv_path (str): Path to output CSV file
            
        Returns:
            bool: True if conversion successful, False otherwise
        """
        try:
            # First try to extract tables
            tables = self.extract_tables_from_pdf(pdf_path)
            
            if tables:
                # If tables found, convert them to CSV
                with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';')
                    
                    for table in tables:
                        for row in table:
                            # Clean up row data
                            cleaned_row = [str(cell).strip() if cell is not None else '' for cell in row]
                            writer.writerow(cleaned_row)
                
                return True
            
            # If no tables found, try to extract text and parse as tabular data
            text = self.extract_text_from_pdf(pdf_path)
            
            # Try to identify tabular patterns in text
            lines = text.split('\n')
            csv_lines = []
            
            for line in lines:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Try to split by common delimiters
                if ';' in line:
                    csv_lines.append(line)
                elif '\t' in line:
                    csv_lines.append(line.replace('\t', ';'))
                elif ',' in line and line.count(',') > 2:
                    # Multiple commas suggest CSV format
                    csv_lines.append(line.replace(',', ';'))
                else:
                    # Treat as a single column
                    csv_lines.append(line)
            
            if csv_lines:
                with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                    for line in csv_lines:
                        csvfile.write(line + '\n')
                
                return True
            
            return False
            
        except Exception as e:
            print(f"Error converting PDF to CSV: {e}")
            return False
    
    def is_pdf_file(self, file_path: str) -> bool:
        """
        Check if file is a PDF
        
        Args:
            file_path (str): Path to file
            
        Returns:
            bool: True if file is PDF, False otherwise
        """
        try:
            with open(file_path, 'rb') as file:
                header = file.read(4)
                return header == b'%PDF'
        except Exception:
            return False

# Test function
if __name__ == "__main__":
    # This is just for testing purposes
    processor = PDFProcessor()
    print("PDF Processor module loaded successfully")