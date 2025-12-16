# test_flask.py
try:
    import flask
    print("✅ Flask is installed!")
    print(f"   Version: {flask.__version__}")
except ImportError:
    print("❌ Flask is NOT installed!")
    print("   Run: pip install flask")
    
import sys
print(f"\nPython version: {sys.version}")