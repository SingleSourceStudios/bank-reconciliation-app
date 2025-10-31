#!/usr/bin/env python3
"""
Run script for Kamel Potteries Bank Reconciliation App
"""
import subprocess
import sys
import os

def main():
    """Run the Streamlit application"""
    try:
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Path to the main app file
        app_path = os.path.join(script_dir, "app.py")
        
        # Run the Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error running the application: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()