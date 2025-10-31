"""
Command-line interface for Kamel Potteries Bank Reconciliation App
"""
import argparse
import os
import sys
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(description="Kamel Potteries Bank Reconciliation Tool")
    parser.add_argument("--bank-file", help="Path to bank statement CSV file")
    parser.add_argument("--xero-file", help="Path to Xero data CSV file")
    parser.add_argument("--output-dir", default="output", help="Directory for output files")
    parser.add_argument("--tolerance-days", type=int, default=3, help="Date tolerance in days")
    parser.add_argument("--tolerance-amount", type=float, default=0.01, help="Amount tolerance")
    
    args = parser.parse_args()
    
    # Check if files are provided
    if not args.bank_file or not args.xero_file:
        parser.print_help()
        return
    
    # Check if files exist
    if not os.path.exists(args.bank_file):
        print(f"Error: Bank file not found: {args.bank_file}")
        return
    
    if not os.path.exists(args.xero_file):
        print(f"Error: Xero file not found: {args.xero_file}")
        return
    
    try:
        # Import modules
        from data_processor import BankStatementProcessor, XeroDataProcessor
        from reconciliation_engine import ReconciliationEngine
        from report_generator import ReportGenerator
        
        print("Loading bank statement data...")
        bank_processor = BankStatementProcessor()
        bank_data = bank_processor.load_data(args.bank_file)
        
        print("Loading Xero data...")
        xero_processor = XeroDataProcessor()
        xero_data = xero_processor.load_data(args.xero_file)
        
        print("Performing reconciliation...")
        engine = ReconciliationEngine(
            tolerance_days=args.tolerance_days,
            tolerance_amount=args.tolerance_amount
        )
        discrepancies = engine.find_discrepancies(bank_data, xero_data)
        
        print(f"Found {len(discrepancies)} discrepancies")
        
        # Create output directory
        os.makedirs(args.output_dir, exist_ok=True)
        
        # Generate reports
        report_gen = ReportGenerator()
        
        # Summary report
        summary_report = report_gen.generate_summary_report(discrepancies)
        summary_path = os.path.join(args.output_dir, f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(summary_path, 'w') as f:
            f.write(summary_report)
        print(f"Summary report saved to: {summary_path}")
        
        # Detailed CSV report
        csv_data = report_gen.generate_detailed_csv(discrepancies)
        csv_path = os.path.join(args.output_dir, f"discrepancies_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        with open(csv_path, 'w') as f:
            f.write(csv_data)
        print(f"Detailed CSV report saved to: {csv_path}")
        
        # Action plan
        action_plan = report_gen.generate_action_plan(discrepancies)
        action_path = os.path.join(args.output_dir, f"action_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(action_path, 'w') as f:
            f.write(action_plan)
        print(f"Action plan saved to: {action_path}")
        
        print("\nReconciliation completed successfully!")
        
    except Exception as e:
        print(f"Error during reconciliation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()