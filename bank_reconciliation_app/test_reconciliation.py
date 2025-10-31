"""
Test script for bank reconciliation functionality
"""
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_data_processing():
    """Test data processing functionality"""
    try:
        from data_processor import BankStatementProcessor, XeroDataProcessor
        
        # Test bank statement processing
        bank_processor = BankStatementProcessor()
        sample_bank_path = os.path.join("data", "sample_data", "sample_bank_statement.csv")
        
        if os.path.exists(sample_bank_path):
            bank_data = bank_processor.load_data(sample_bank_path)
            print(f"Bank statement loaded successfully: {len(bank_data)} transactions")
            print(f"Date range: {bank_data['Date'].min()} to {bank_data['Date'].max()}")
        else:
            print("Sample bank statement file not found")
            
        # Test Xero data processing
        xero_processor = XeroDataProcessor()
        sample_xero_path = os.path.join("data", "sample_data", "sample_xero_data.csv")
        
        if os.path.exists(sample_xero_path):
            xero_data = xero_processor.load_data(sample_xero_path)
            print(f"Xero data loaded successfully: {len(xero_data)} transactions")
            print(f"Date range: {xero_data['Date'].min()} to {xero_data['Date'].max()}")
        else:
            print("Sample Xero data file not found")
            
    except Exception as e:
        print(f"Error in data processing test: {e}")

def test_reconciliation():
    """Test reconciliation functionality"""
    try:
        from data_processor import BankStatementProcessor, XeroDataProcessor
        from reconciliation_engine import ReconciliationEngine
        
        # Load sample data
        bank_processor = BankStatementProcessor()
        xero_processor = XeroDataProcessor()
        
        sample_bank_path = os.path.join("data", "sample_data", "sample_bank_statement.csv")
        sample_xero_path = os.path.join("data", "sample_data", "sample_xero_data.csv")
        
        if os.path.exists(sample_bank_path) and os.path.exists(sample_xero_path):
            bank_data = bank_processor.load_data(sample_bank_path)
            xero_data = xero_processor.load_data(sample_xero_path)
            
            # Perform reconciliation
            engine = ReconciliationEngine()
            discrepancies = engine.find_discrepancies(bank_data, xero_data)
            
            print(f"Reconciliation completed: {len(discrepancies)} discrepancies found")
            
            # Show discrepancy types
            types = {}
            for disc in discrepancies:
                disc_type = disc['type']
                types[disc_type] = types.get(disc_type, 0) + 1
            
            for disc_type, count in types.items():
                print(f"  {disc_type}: {count}")
        else:
            print("Sample data files not found")
            
    except Exception as e:
        print(f"Error in reconciliation test: {e}")

def test_report_generation():
    """Test report generation functionality"""
    try:
        from report_generator import ReportGenerator
        
        # Create sample discrepancies
        sample_discrepancies = [
            {
                'type': 'unmatched_bank',
                'date': '2025-06-12',
                'amount': 5000.00,
                'description': 'Sales Revenue',
                'reference': 'INV-001',
                'payee': 'Unknown Customer',
                'details': 'Transaction found in bank statement but not in Xero'
            },
            {
                'type': 'unmatched_xero',
                'date': '2025-06-18',
                'amount': -1500.00,
                'description': 'Office Supplies Purchase',
                'reference': 'PO-123',
                'payee': 'Office Supplier',
                'details': 'Transaction found in Xero but not in bank statement'
            }
        ]
        
        report_gen = ReportGenerator()
        summary = report_gen.generate_summary_report(sample_discrepancies)
        print("Sample Summary Report:")
        print("=" * 50)
        print(summary)
        
    except Exception as e:
        print(f"Error in report generation test: {e}")

if __name__ == "__main__":
    print("Testing Bank Reconciliation App Components")
    print("=" * 50)
    
    print("\n1. Testing Data Processing...")
    test_data_processing()
    
    print("\n2. Testing Reconciliation Engine...")
    test_reconciliation()
    
    print("\n3. Testing Report Generation...")
    test_report_generation()
    
    print("\nTesting completed.")