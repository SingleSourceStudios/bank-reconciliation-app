# Kamel Potteries Bank Reconciliation App

This application helps reconcile bank statements with Xero accounting data to identify discrepancies and ensure financial accuracy. It now supports both CSV and PDF file formats for easier data import.

## Features

- Upload bank statements and Xero data in CSV or PDF format
- Automatically match transactions based on date and amount
- Identify unmatched transactions in both systems
- Generate detailed reports of discrepancies
- Provide action plans for resolving discrepancies
- Automatic PDF to CSV conversion for data processing

## Installation

1. Navigate to the bank_reconciliation_app directory:
   ```
   cd /Users/rain-c/Documents/kamel-app/bank_reconciliation_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

2. Open your web browser to the URL provided (typically http://localhost:8501)

3. Upload your bank statement and Xero data files (CSV or PDF format)

4. View the reconciliation results and download reports

## File Formats

### Bank Statement Format
The bank statement should be in CSV format with the following columns (PDF files will be automatically converted to this format):
- Date (DD/MM/YYYY format)
- Amount (numeric, negative for debits, positive for credits)
- Payee (optional)
- Description (optional)
- Reference (optional)
- Check Number (optional)

Example:
```
*Date;*Amount;Payee;Description;Reference;Check Number
1/06/2025;-160.00;Headoffice;Monthly Acc Fee Headoffice *;;
1/06/2025;-767.00;Headoffice;Transaction Charge Headoffice *;;
```

### Xero Data Format
Xero data should be exported in CSV format with similar columns (PDF files will be automatically converted to this format):
- Date
- Amount
- Payee
- Description
- Reference
- Check Number

## How It Works

1. **Data Processing**: The app loads and processes both bank statement and Xero data, converting dates and amounts to standard formats.

2. **Transaction Matching**: Transactions are matched based on:
   - Date (within a 3-day tolerance)
   - Amount (within a R0.01 tolerance)

3. **Discrepancy Identification**: The app identifies:
   - Unmatched bank transactions (in bank but not Xero)
   - Unmatched Xero transactions (in Xero but not bank)
   - Potential duplicates

4. **Reporting**: Detailed reports are generated with:
   - Summary statistics
   - List of all discrepancies
   - Action plan for resolution

## Support

For issues or questions, please contact the Kamel Potteries finance team.