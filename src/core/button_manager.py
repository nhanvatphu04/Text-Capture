"""
Button management utilities for enabling/disabling buttons
"""


class ButtonManager:
    """Manages button states and connections"""
    
    def __init__(self, buttons):
        self.buttons = buttons
        self.action_thread = None
    
    def disable_other_buttons(self, active_button):
        """Disable tất cả buttons trừ button đang được click"""
        for button in self.buttons:
            if button != active_button:
                button.setEnabled(False)
                button.setStyleSheet("QPushButton:disabled { background-color: #f0f0f0; color: #a0a0a0; }")

    def enable_all_buttons(self):
        """Enable lại tất cả buttons"""
        for button in self.buttons:
            button.setEnabled(True)
            button.setStyleSheet("")  # Reset về style mặc định

    def on_action_finished(self):
        """Callback khi action hoàn thành"""
        self.enable_all_buttons() 