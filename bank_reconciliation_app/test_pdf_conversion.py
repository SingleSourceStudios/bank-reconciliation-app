"""
Test script for PDF to CSV conversion
"""
import os
from pdf_processor import PDFProcessor

def create_sample_pdf():
    """Create a simple test PDF with tabular data"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        # Create a simple PDF with tabular data
        pdf_path = os.path.join("data", "sample_data", "test_bank_statement.pdf")
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        
        # Add title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Test Bank Statement")
        
        # Add table headers
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, height - 100, "Date")
        c.drawString(150, height - 100, "Amount")
        c.drawString(250, height - 100, "Description")
        c.drawString(400, height - 100, "Reference")
        
        # Add some sample data
        c.setFont("Helvetica", 10)
        data = [
            ("01/06/2025", "-160.00", "Monthly Account Fee", "FEE001"),
            ("01/06/2025", "-767.00", "Transaction Charge", "CHG001"),
            ("01/06/2025", "900.60", "Credit Payment", "CR001"),
            ("02/06/2025", "-182.59", "POS Purchase", "POS001"),
            ("05/06/2025", "133004.17", "Settlement", "SET001"),
        ]
        
        y_position = height - 130
        for date, amount, desc, ref in data:
            c.drawString(50, y_position, date)
            c.drawString(150, y_position, amount)
            c.drawString(250, y_position, desc)
            c.drawString(400, y_position, ref)
            y_position -= 20
        
        c.save()
        print(f"Sample PDF created at: {pdf_path}")
        return pdf_path
    except ImportError:
        print("ReportLab not installed. Creating a simple text file instead.")
        # Create a simple text file that looks like a PDF for testing
        pdf_path = os.path.join("data", "sample_data", "test_bank_statement.pdf")
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        
        # Just create an empty file for now
        with open(pdf_path, 'w') as f:
            f.write("%PDF-1.4\n")
            f.write("This is a test PDF file for conversion testing.\n")
            f.write("Date;Amount;Description;Reference\n")
            f.write("01/06/2025;-160.00;Monthly Account Fee;FEE001\n")
            f.write("01/06/2025;-767.00;Transaction Charge;CHG001\n")
            f.write("01/06/2025;900.60;Credit Payment;CR001\n")
        print(f"Simple test PDF created at: {pdf_path}")
        return pdf_path

def test_pdf_conversion():
    """Test PDF to CSV conversion"""
    print("Testing PDF to CSV conversion...")
    
    # Create sample PDF
    pdf_path = create_sample_pdf()
    
    # Convert to CSV
    csv_path = os.path.join("data", "sample_data", "test_bank_statement.csv")
    processor = PDFProcessor()
    
    try:
        success = processor.pdf_to_csv(pdf_path, csv_path)
        if success:
            print(f"PDF successfully converted to CSV: {csv_path}")
            
            # Show the content of the CSV
            print("\nCSV Content:")
            with open(csv_path, 'r') as f:
                content = f.read()
                print(content)
        else:
            print("PDF conversion failed.")
    except Exception as e:
        print(f"Error during PDF conversion: {e}")

if __name__ == "__main__":
    test_pdf_conversion()