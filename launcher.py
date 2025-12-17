"""
Launcher script for the Entity Recognition System
This script handles the setup and launches the web application
"""

import os
import sys
import subprocess
import webbrowser
import time
import threading
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        input("Press Enter to exit...")
        sys.exit(1)

def install_requirements():
    """Install required packages if not already installed"""
    try:
        import flask
        import spacy
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "flask", "flask-cors", "spacy", "gunicorn", "python-dotenv"])

def download_spacy_model():
    """Download spaCy language model if not present"""
    try:
        import spacy
        try:
            spacy.load('en_core_web_lg')
        except OSError:
            print("Downloading spaCy language model...")
            subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_lg"])
    except Exception as e:
        print(f"Warning: Could not download spaCy model: {e}")

def start_flask_app():
    """Start the Flask application"""
    try:
        # Import the app module
        from app import app

        # Run the app
        print("=" * 60)
        print("ENTITY RECOGNITION SYSTEM")
        print("=" * 60)
        print("\nStarting web server...")
        print("The application will open in your default browser automatically.")
        print("If it doesn't open, visit: http://localhost:5000")
        print("\nPress Ctrl+C to stop the server\n")

        # Start browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open('http://localhost:5000')

        threading.Thread(target=open_browser, daemon=True).start()

        # Run the Flask app
        app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)

    except Exception as e:
        print(f"Error starting application: {e}")
        input("Press Enter to exit...")

def main():
    """Main launcher function"""
    print("Entity Recognition System Launcher")
    print("==================================")

    # Check Python version
    check_python_version()

    # Install requirements
    install_requirements()

    # Download spaCy model
    download_spacy_model()

    # Start the Flask app
    start_flask_app()

if __name__ == "__main__":
    main()