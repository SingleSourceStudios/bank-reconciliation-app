"""
Bank Statement Reconciliation Application
Matches bank statements with Xero accounting data to identify discrepancies
"""
import streamlit as st
import os
from datetime import datetime

# Import our modules (these will be resolved when dependencies are installed)
try:
    from data_processor import BankStatementProcessor, XeroDataProcessor
    from reconciliation_engine import ReconciliationEngine
    from report_generator import ReportGenerator
    from pdf_processor import PDFProcessor
    DEPENDENCIES_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    DEPENDENCIES_AVAILABLE = False

def check_dependencies():
    """Check if required dependencies are available"""
    dependencies = ['pandas', 'numpy']
    missing = []
    
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            missing.append(dep)
    
    return missing

def main():
    st.set_page_config(
        page_title="Kamel Potteries Bank Reconciliation",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("🏦 Kamel Potteries Bank Statement Reconciliation")
    
    # Check for dependencies
    missing_deps = check_dependencies()
    if missing_deps:
        st.error(f"Missing required dependencies: {', '.join(missing_deps)}")
        st.info("Please install required dependencies using: pip install pandas numpy streamlit")
        return
    
    st.markdown("""
    This application matches bank statements with Xero accounting data to identify discrepancies.
    Upload your bank statement and Xero data to begin the reconciliation process.
    """)
    
    # Create tabs for different functionalities
    tab1, tab2, tab3 = st.tabs(["Upload Data", "Reconciliation Results", "Reports"])
    
    with tab1:
        upload_data()
    
    with tab2:
        show_reconciliation_results()
        
    with tab3:
        generate_reports()

def upload_data():
    st.header("Upload Financial Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Bank Statement")
        bank_file = st.file_uploader(
            "Upload Bank Statement (CSV or PDF format)",
            type=["csv", "pdf"],
            key="bank_upload"
        )
        
        if bank_file is not None:
            # Handle file upload
            file_extension = bank_file.name.split('.')[-1].lower()
            original_path = os.path.join("data", "uploads", f"bank_statement.{file_extension}")
            csv_path = os.path.join("data", "uploads", "bank_statement.csv")
            
            os.makedirs(os.path.dirname(original_path), exist_ok=True)
            
            # Save original file
            with open(original_path, "wb") as f:
                f.write(bank_file.getbuffer())
            
            # If PDF, convert to CSV
            if file_extension == "pdf":
                try:
                    pdf_processor = PDFProcessor()
                    # Try specialized bank statement processing first
                    if pdf_processor.process_bank_statement_pdf(original_path, csv_path):
                        st.success("Bank statement PDF converted to CSV successfully!")
                        st.session_state.bank_uploaded = True
                    else:
                        # Fallback to general PDF processing
                        if pdf_processor.pdf_to_csv(original_path, csv_path):
                            st.success("Bank statement PDF converted to CSV successfully!")
                            st.session_state.bank_uploaded = True
                        else:
                            st.error("Failed to convert PDF to CSV. Please ensure the PDF contains tabular data.")
                except Exception as e:
                    st.error(f"Error processing PDF file: {str(e)}")
            else:
                # For CSV, just copy to the expected location
                import shutil
                shutil.copy2(original_path, csv_path)
                st.success("Bank statement uploaded successfully!")
                st.session_state.bank_uploaded = True
    
    with col2:
        st.subheader("Xero Data")
        xero_file = st.file_uploader(
            "Upload Xero Data (CSV or PDF format)",
            type=["csv", "pdf"],
            key="xero_upload"
        )
        
        if xero_file is not None:
            # Handle file upload
            file_extension = xero_file.name.split('.')[-1].lower()
            original_path = os.path.join("data", "uploads", f"xero_data.{file_extension}")
            csv_path = os.path.join("data", "uploads", "xero_data.csv")
            
            os.makedirs(os.path.dirname(original_path), exist_ok=True)
            
            # Save original file
            with open(original_path, "wb") as f:
                f.write(xero_file.getbuffer())
            
            # If PDF, convert to CSV
            if file_extension == "pdf":
                try:
                    pdf_processor = PDFProcessor()
                    # Try specialized Xero processing first
                    if pdf_processor.process_xero_pdf(original_path, csv_path):
                        st.success("Xero data PDF converted to CSV successfully!")
                        st.session_state.xero_uploaded = True
                    else:
                        # Fallback to general PDF processing
                        if pdf_processor.pdf_to_csv(original_path, csv_path):
                            st.success("Xero data PDF converted to CSV successfully!")
                            st.session_state.xero_uploaded = True
                        else:
                            st.error("Failed to convert PDF to CSV. Please ensure the PDF contains tabular data.")
                except Exception as e:
                    st.error(f"Error processing PDF file: {str(e)}")
            else:
                # For CSV, just copy to the expected location
                import shutil
                shutil.copy2(original_path, csv_path)
                st.success("Xero data uploaded successfully!")
                st.session_state.xero_uploaded = True

def show_reconciliation_results():
    st.header("Reconciliation Results")
    
    # Debug information
    st.write(f"Bank uploaded: {st.session_state.get('bank_uploaded', False)}")
    st.write(f"Xero uploaded: {st.session_state.get('xero_uploaded', False)}")
    st.write(f"Discrepancies in session: {'discrepancies' in st.session_state}")
    
    # Check if both files are uploaded
    if not (st.session_state.get('bank_uploaded', False) and st.session_state.get('xero_uploaded', False)):
        st.info("Please upload both bank statement and Xero data in the 'Upload Data' tab.")
        return
    
    # Always show the manual trigger button
    st.info("Click the button below to perform reconciliation")
    if st.button("Perform Reconciliation", type="primary", use_container_width=True):
        perform_reconciliation()
    
    # Display results
    if 'discrepancies' in st.session_state:
        discrepancies = st.session_state.discrepancies
        
        # Calculate counts
        unmatched_bank_count = len([d for d in discrepancies if d['type'] == 'unmatched_bank'])
        unmatched_xero_count = len([d for d in discrepancies if d['type'] == 'unmatched_xero'])
        total_discrepancies = unmatched_bank_count + unmatched_xero_count
        
        st.subheader(f"Found {total_discrepancies} Total Discrepancies")
        
        # Summary metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Discrepancies", total_discrepancies)
        col2.metric("Unmatched Bank Entries", unmatched_bank_count)
        col3.metric("Unmatched Xero Entries", unmatched_xero_count)
        
        # Show additional info about duplicates
        duplicate_bank_count = len([d for d in discrepancies if d['type'] == 'duplicate_bank'])
        duplicate_xero_count = len([d for d in discrepancies if d['type'] == 'duplicate_xero'])
        if duplicate_bank_count > 0 or duplicate_xero_count > 0:
            st.info(f"Note: Found {duplicate_bank_count} potential duplicate bank transactions and {duplicate_xero_count} potential duplicate Xero transactions")
        
        # Display discrepancies in a table
        if discrepancies:
            try:
                import pandas as pd
                df_discrepancies = pd.DataFrame(discrepancies)
                st.dataframe(df_discrepancies, use_container_width=True)
                
                # Filter by type
                discrepancy_types = list(set([d['type'] for d in discrepancies]))
                selected_types = st.multiselect("Filter by discrepancy type", discrepancy_types, default=discrepancy_types)
                
                filtered_discrepancies = [d for d in discrepancies if d['type'] in selected_types]
                st.dataframe(pd.DataFrame(filtered_discrepancies), use_container_width=True)
            except Exception as e:
                st.error(f"Error displaying data: {str(e)}")

def perform_reconciliation():
    # Process the data
    try:
        with st.spinner("Processing data and performing reconciliation..."):
            # Initialize processors
            bank_processor = BankStatementProcessor()
            xero_processor = XeroDataProcessor()
            
            # Load data
            bank_path = os.path.join("data", "uploads", "bank_statement.csv")
            xero_path = os.path.join("data", "uploads", "xero_data.csv")
            
            bank_data = bank_processor.load_data(bank_path)
            xero_data = xero_processor.load_data(xero_path)
            
            # Perform reconciliation
            engine = ReconciliationEngine()
            discrepancies = engine.find_discrepancies(bank_data, xero_data)
            
            # Store results in session state
            st.session_state.discrepancies = discrepancies
            st.session_state.bank_data = bank_data
            st.session_state.xero_data = xero_data
            
            st.success("Reconciliation completed successfully!")
            
    except Exception as e:
        st.error(f"Error during reconciliation: {str(e)}")
        return

def generate_reports():
    st.header("Discrepancy Reports")
    
    if 'discrepancies' not in st.session_state:
        st.info("Please complete the reconciliation process first.")
        return
    
    discrepancies = st.session_state.discrepancies
    
    # Generate summary report
    try:
        report_gen = ReportGenerator()
        summary_report = report_gen.generate_summary_report(discrepancies)
        
        st.subheader("Summary Report")
        st.text(summary_report)
        
        # Download options
        st.subheader("Download Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Download Detailed Report (CSV)"):
                csv_data = report_gen.generate_detailed_csv(discrepancies)
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name=f"discrepancies_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        with col2:
            if st.button("Download Action Plan (TXT)"):
                action_plan = report_gen.generate_action_plan(discrepancies)
                st.download_button(
                    label="Download Action Plan",
                    data=action_plan,
                    file_name=f"action_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
        
        # Display action recommendations
        st.subheader("Recommended Actions")
        recommendations = report_gen.get_recommendations(discrepancies)
        for rec in recommendations:
            st.markdown(f"- {rec}")
    except Exception as e:
        st.error(f"Error generating reports: {str(e)}")

if __name__ == "__main__":
    main()