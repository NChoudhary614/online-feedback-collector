import subprocess
import sys

# Try to import flask
try:
    from flask import Flask
    print("✅ Flask is already installed")
except ImportError:
    print("❌ Flask not found. Installing...")
    # Install flask
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    print("✅ Flask installed successfully!")
    
# Now run your app
from app import app

if __name__ == "__main__":
    app.run(debug=True, port=5000)