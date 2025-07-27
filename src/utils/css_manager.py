"""
CSS Property Manager for Qt Widgets
"""

from PySide6.QtWidgets import QWidget
from typing import Any, Optional


class CSSManager:
    """Utility class for managing CSS properties and states"""
    
    @staticmethod
    def set_property(widget: QWidget, property_name: str, value: Any) -> None:
        """
        Set a CSS property for a widget and update its style
        
        Args:
            widget: The widget to update
            property_name: Name of the CSS property
            value: Value to set for the property
        """
        widget.setProperty(property_name, value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)


class WidgetStateManager:
    """Manager for widget states with predefined CSS properties"""
    
    def __init__(self, widget: QWidget):
        self.widget = widget
        self.css_manager = CSSManager()
    
    def set_loading_state(self, loading: bool = True) -> None:
        """Set loading state for the widget"""
        self.css_manager.set_property(self.widget, "loading", loading)
    
    def set_error_state(self, error: bool = True) -> None:
        """Set error state for the widget"""
        self.css_manager.set_property(self.widget, "error", error)
    
    def set_success_state(self, success: bool = True) -> None:
        """Set success state for the widget"""
        self.css_manager.set_property(self.widget, "success", success)
    
    def set_drag_over_state(self, drag_over: bool = True) -> None:
        """Set drag over state for the widget"""
        self.css_manager.set_property(self.widget, "dragOver", drag_over)
    
    def set_processing_state(self, processing: bool = True) -> None:
        """Set processing state for the widget"""
        self.css_manager.set_property(self.widget, "processing", processing)
    
    def set_readonly_state(self, readonly: bool = True) -> None:
        """Set readonly state for the widget"""
        self.css_manager.set_property(self.widget, "readonly", readonly)
    
    def clear_all_states(self) -> None:
        """Clear all state properties"""
        properties_to_clear = [
            "loading", "error", "success", "dragOver", 
            "processing", "readonly"
        ]
        for property_name in properties_to_clear:
            self.widget.setProperty(property_name, None)
        
        self.widget.style().unpolish(self.widget)
        self.widget.style().polish(self.widget)
    
    def reset_to_default(self) -> None:
        """Reset widget to default state"""
        self.clear_all_states() 