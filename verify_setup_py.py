#!/usr/bin/env python3
"""
Setup verification script for gene expression analysis pipeline.
Checks if all required packages are installed correctly.
"""

import sys

def check_package(package_name, import_name=None):
    """Check if a package is installed and importable."""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✓ {package_name} installed successfully")
        return True
    except ImportError:
        print(f"✗ {package_name} NOT installed")
        return False

def main():
    print("Checking Python environment setup...")
    print(f"Python version: {sys.version}\n")
    
    packages = [
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("scipy", "scipy"),
        ("scikit-learn", "sklearn"),
        ("statsmodels", "statsmodels"),
        ("GEOparse", "GEOparse"),
        ("biopython", "Bio"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("plotly", "plotly"),
        ("jupyter", "jupyter"),
    ]
    
    results = []
    print("Package Installation Status:")
    print("-" * 40)
    
    for package_name, import_name in packages:
        results.append(check_package(package_name, import_name))
    
    print("-" * 40)
    
    if all(results):
        print("\n✓ All packages installed successfully!")
        print("You're ready to start the gene expression analysis project.")
        return 0
    else:
        print("\n✗ Some packages are missing.")
        print("Run: pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())