# Kamel Potteries Bank Reconciliation App - Technical Documentation

## Application Structure

```
bank_reconciliation_app/
├── app.py                 # Main Streamlit application
├── cli.py                 # Command-line interface
├── config.py              # Configuration settings
├── data_processor.py      # Data processing modules
├── reconciliation_engine.py # Core reconciliation logic
├── report_generator.py    # Report generation functionality
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup file
├── run_app.py            # Application runner script
├── test_reconciliation.py # Test scripts
├── utils.py              # Utility functions
├── README.md             # User guide
├── DOCUMENTATION.md      # Technical documentation
├── data/                 # Data directory
│   ├── uploads/          # User uploaded files
│   └── sample_data/      # Sample data for testing
├── output/               # Generated reports and output
└── __init__.py           # Package initialization
```

## Core Components

### 1. Data Processor (`data_processor.py`)

Handles loading and preprocessing of bank statement and Xero data:
- `BankStatementProcessor`: Processes bank statement CSV files
- `XeroDataProcessor`: Processes Xero data CSV files
- Normalizes date formats and amount values
- Cleans and validates data

### 2. Reconciliation Engine (`reconciliation_engine.py`)

Core logic for matching transactions:
- Matches transactions based on date (with tolerance) and amount
- Identifies unmatched transactions in both systems
- Detects potential duplicates
- Uses configurable tolerance settings

### 3. Report Generator (`report_generator.py`)

Creates various reports from reconciliation results:
- Summary reports with key metrics
- Detailed CSV exports
- Action plans for resolving discrepancies
- Recommendations for process improvements

### 4. Configuration (`config.py`)

Centralized configuration settings:
- Tolerance values for matching
- File paths and directory structures
- Column mappings for different data formats

### 5. Utilities (`utils.py`)

Common helper functions:
- Currency and date formatting
- File validation and information
- CSV file discovery
- Dataframe comparison

## Data Flow

1. **Input**: User uploads bank statement and Xero CSV files
2. **Processing**: Data processors clean and normalize the data
3. **Matching**: Reconciliation engine matches transactions
4. **Analysis**: Discrepancies are identified and categorized
5. **Reporting**: Reports are generated in various formats
6. **Output**: Results are displayed in UI or saved to files

## Matching Algorithm

The reconciliation engine uses a two-step matching process:

1. **Primary Matching**: 
   - Compare transaction dates within a tolerance window (default: 3 days)
   - Compare transaction amounts within a tolerance (default: R0.01)
   - Match transactions that satisfy both criteria

2. **Discrepancy Identification**:
   - Unmatched bank transactions (in bank but not Xero)
   - Unmatched Xero transactions (in Xero but not bank)
   - Duplicate transactions (same date and amount)

## File Formats

### Bank Statement CSV
Expected format with semicolon separator:
```
*Date;*Amount;Payee;Description;Reference;Check Number
1/06/2025;-160.00;Headoffice;Monthly Acc Fee;;
```

### Xero Data CSV
Expected format with comma separator:
```
Date,Amount,Payee,Description,Reference,Check Number
2025-06-01,-160.00,Headoffice,Monthly Acc Fee,,
```

## Tolerance Settings

- **Date Tolerance**: Maximum difference in days between transactions (default: 3 days)
- **Amount Tolerance**: Maximum difference in amount values (default: R0.01)

## Error Handling

The application includes comprehensive error handling:
- File not found errors
- Data format validation
- Processing errors with descriptive messages
- Graceful degradation when optional features are missing

## Testing

The application includes a test script (`test_reconciliation.py`) that:
- Tests data processing functionality
- Tests reconciliation engine
- Tests report generation
- Validates core functionality with sample data

## Deployment

The application can be run in two modes:
1. **Web Interface**: Using Streamlit for interactive use
2. **Command Line**: For automated processing and batch operations

## Dependencies

- pandas: Data processing and analysis
- numpy: Numerical operations
- streamlit: Web interface framework
- openpyxl: Excel file support (optional)

## Future Enhancements

Potential improvements for future versions:
- Integration with Xero API for direct data access
- Machine learning for improved matching accuracy
- Email notifications for discrepancy alerts
- Database storage for historical reconciliation data
- Multi-currency support
- Enhanced reporting with charts and visualizations