#!/usr/bin/env python3
"""
Runner for COVID Prediction Dashboard - FIXED VERSION
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

print("="*60)
print("🚀 COVID-19 PREDICTION DASHBOARD")
print("="*60)

def check_app_structure():
    """Check if the app directory has all required files"""
    print("🔍 Checking app structure...")
    
    # Check INSIDE the app directory
    app_path = os.path.join(os.path.dirname(__file__), 'app')
    required_files = [
        ('app.py', 'file'),
        ('models.py', 'file'),
        ('templates/', 'directory'),
        ('static/', 'directory')
    ]
    
    all_ok = True
    for filename, filetype in required_files:
        full_path = os.path.join(app_path, filename)
        exists = os.path.exists(full_path)
        status = "✅" if exists else "❌"
        print(f"   {status} app/{filename} ({filetype})")
        if not exists:
            all_ok = False
    
    return all_ok

# Check if app structure is correct
if not check_app_structure():
    print("\n⚠️  Some files are missing in the app/ directory!")
    print("💡 Make sure you have:")
    print("   - app/templates/ directory")
    print("   - app/static/ directory")
    print("   - app/app.py file")
    print("   - app/models.py file")
    sys.exit(1)

try:
    # Import the Flask app from app/app.py
    from app import app
    print("✅ Successfully imported Flask app")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("\n💡 Possible solutions:")
    print("   1. Make sure app/app.py exists")
    print("   2. Check that app/app.py has: app = Flask(__name__)")
    print("   3. Verify __init__.py exists in app/ folder")
    
    # Try creating __init__.py if missing
    init_file = os.path.join('app', '__init__.py')
    if not os.path.exists(init_file):
        print(f"\n📄 Creating {init_file}...")
        with open(init_file, 'w') as f:
            f.write("# This makes app a Python package\n")
        print("✅ Created __init__.py")
    
    sys.exit(1)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("📊 Open: http://localhost:5000")
    print("🎯 Dashboard Features:")
    print("   • Real-time COVID-19 Prediction")
    print("   • 6 Machine Learning Algorithms")
    print("   • Interactive Symptom Selection")
    print("   • Model Comparison Charts")
    print("="*60)
    
    try:
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
    except KeyboardInterrupt:
        print("\n\n👋 Dashboard stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")