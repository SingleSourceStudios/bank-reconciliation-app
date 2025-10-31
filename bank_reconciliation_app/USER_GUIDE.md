# Kamel Potteries Bank Reconciliation App - User Guide

## Overview

This application helps reconcile bank statements with Xero accounting data to identify discrepancies and ensure financial accuracy. It provides both a web interface and command-line interface for flexible usage. The application now supports both CSV and PDF file formats for easier data import.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. Navigate to the application directory:
   ```bash
   cd /Users/rain-c/Documents/kamel-app/bank_reconciliation_app
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or use the provided scripts:
   - On macOS/Linux: `./run.sh`
   - On Windows: `run.bat`

## Using the Web Interface

### Starting the Application

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser to the URL provided (typically http://localhost:8501)

### Uploading Data

1. Navigate to the "Upload Data" tab
2. Upload your bank statement file (CSV or PDF format)
3. Upload your Xero data file (CSV or PDF format)
4. PDF files will be automatically converted to CSV for processing

### Viewing Results

1. Switch to the "Reconciliation Results" tab
2. View summary metrics and discrepancy details
3. Filter discrepancies by type using the multiselect widget

### Generating Reports

1. Navigate to the "Reports" tab
2. View the summary report
3. Download detailed reports in CSV format
4. Download action plans in TXT format

## Using the Command Line Interface

### Basic Usage

```bash
python cli.py --bank-file bank.csv --xero-file xero.csv
```

### Advanced Options

```bash
python cli.py \
  --bank-file bank.csv \
  --xero-file xero.csv \
  --output-dir reports \
  --tolerance-days 5 \
  --tolerance-amount 0.05
```

### CLI Parameters

- `--bank-file`: Path to bank statement CSV file
- `--xero-file`: Path to Xero data CSV file
- `--output-dir`: Directory for output files (default: "output")
- `--tolerance-days`: Date tolerance in days (default: 3)
- `--tolerance-amount`: Amount tolerance (default: 0.01)

## File Formats

### Bank Statement Format

The bank statement should be in CSV format with semicolon separators (PDF files will be automatically converted to this format):

```
*Date;*Amount;Payee;Description;Reference;Check Number
1/06/2025;-160.00;Headoffice;Monthly Acc Fee Headoffice *;;
```

Required columns:
- Date (DD/MM/YYYY format)
- Amount (negative for debits, positive for credits)

### Xero Data Format

Xero data should be in CSV format with comma separators (PDF files will be automatically converted to this format):

```
Date,Amount,Payee,Description,Reference,Check Number
2025-06-01,-160.00,Headoffice,Monthly Acc Fee Headoffice,,
```

Required columns:
- Date (YYYY-MM-DD format)
- Amount (negative for expenses, positive for income)

## Understanding the Results

### Discrepancy Types

1. **Unmatched Bank**: Transactions in bank statement but not in Xero
2. **Unmatched Xero**: Transactions in Xero but not in bank statement
3. **Duplicate Bank**: Potential duplicate transactions in bank statement
4. **Duplicate Xero**: Potential duplicate transactions in Xero data

### Key Metrics

- **Total Discrepancies**: Overall count of issues found
- **Unmatched Bank Entries**: Transactions missing from Xero
- **Unmatched Xero Entries**: Transactions missing from bank

## Troubleshooting

### Common Issues

1. **"Module not found" errors**: Run `pip install -r requirements.txt`

2. **File format errors**: Ensure CSV files are properly formatted with correct separators

3. **Date parsing errors**: Check that dates are in the expected format

4. **Permission errors**: Ensure you have write permissions to the output directory

### Getting Help

For issues or questions, please contact the Kamel Potteries finance team.

## Best Practices

1. **Regular Reconciliation**: Run reconciliation monthly or quarterly
2. **Data Backup**: Keep backups of original bank and Xero data
3. **Consistent Naming**: Use consistent file naming conventions
4. **Documentation**: Keep records of discrepancy resolutions
5. **Validation**: Always verify discrepancy findings before making adjustments

## Sample Data

The application includes sample data files for testing:
- `data/sample_data/sample_bank_statement.csv`
- `data/sample_data/sample_xero_data.csv`

To test with sample data:
```bash
python cli.py \
  --bank-file data/sample_data/sample_bank_statement.csv \
  --xero-file data/sample_data/sample_xero_data.csv
```

## Customization

### Adjusting Tolerance Settings

Modify matching sensitivity:
- Increase `tolerance-days` for more flexible date matching
- Increase `tolerance-amount` for more flexible amount matching

### Configuration File

Edit `config.py` to modify:
- Default file paths
- Date formats
- Column mappings
- Output settings

## Security

- All data processing happens locally on your computer
- No data is transmitted to external servers
- Files are processed in memory and not stored permanently
- Temporary files are automatically cleaned up

## Support

For technical support, please contact the development team.
For business process questions, please contact the finance team.