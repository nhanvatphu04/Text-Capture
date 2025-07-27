"""
Button management utilities for enabling/disabling buttons
"""


class ButtonManager:
    """Manages button states and connections"""
    
    def __init__(self, buttons):
        self.buttons = buttons
        self.action_thread = None
    
    def disable_other_buttons(self, active_button):
        """Disable all buttons except the active one"""
        for button in self.buttons:
            if button != active_button:
                button.setEnabled(False)
                # Set disabled class instead of inline style
                button.setProperty("class", "disabled")
                button.style().unpolish(button)
                button.style().polish(button)

    def enable_all_buttons(self):
        """Enable all buttons"""
        for button in self.buttons:
            button.setEnabled(True)
            # Reset to default class
            button.setProperty("class", "")
            button.style().unpolish(button)
            button.style().polish(button)

    def on_action_finished(self):
        """Callback when action is finished"""
        self.enable_all_buttons() 