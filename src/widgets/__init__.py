# Widgets package
# Export main widgets for easy importing

"""
import sys
import os
# Add src directory to path to import resources_rc
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import resources_rc
"""

from .mainwindow.ui_form import Ui_Main

__all__ = ['Ui_Main']
