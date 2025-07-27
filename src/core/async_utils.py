"""
Async utilities for handling button actions in separate threads
"""
from functools import wraps
from PySide6.QtCore import QThread, SIGNAL


def async_action(func):
    """Decorator để chạy action trong thread riêng và tự động enable lại buttons"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Disable tất cả buttons trừ button hiện tại
        self.main_window.disable_other_buttons(self.main_window.sender())
        
        # Tạo thread để chạy action
        self.main_window.action_thread = ActionThread(func, self, *args, **kwargs)
        self.main_window.action_thread.connect(SIGNAL("finished()"), self.main_window.on_action_finished)
        self.main_window.action_thread.start()
        
    return wrapper


class ActionThread(QThread):
    """Thread để chạy các action không đồng bộ"""
    
    def __init__(self, func, instance, *args, **kwargs):
        super().__init__()
        self.func = func
        self.instance = instance
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        try:
            self.func(self.instance, *self.args, **self.kwargs)
        except Exception as e:
            print(f"Error in action: {e}")
        finally:
            self.emit(SIGNAL("finished()")) 