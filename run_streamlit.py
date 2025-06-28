import subprocess
import sys
import os

def run_streamlit():
    """Launch the Streamlit application"""
    print("🚀 Launching Flight Hazard Alert System...")
    print("📱 Opening web interface in your browser...")
    print("🌐 If browser doesn't open automatically, go to: http://localhost:8501")
    print("\n" + "="*50)
    
    # Run streamlit
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
        "--server.port", "8501",
        "--server.address", "localhost"
    ])

if __name__ == "__main__":
    run_streamlit() 