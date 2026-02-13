import subprocess
import sys
import os

# Start Streamlit on port 8001 (the backend port)
if __name__ == "__main__":
    os.chdir("c:/Users/rahul/OneDrive/Documents/streamlit/")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "master6.py",
            "--server.port=8001",
            "--server.address=0.0.0.0",
            "--server.headless=true",
            "--browser.gatherUsageStats=false",
            "--server.enableCORS=true",
            "--server.enableXsrfProtection=false",
        ]
    )
