"""
Main entry point for TextCapture application
"""

import sys
import os

# Add app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src import run_app

if __name__ == "__main__":
    sys.exit(run_app())
