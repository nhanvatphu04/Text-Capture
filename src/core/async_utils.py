"""
Async utilities for handling button actions in separate threads
"""

import time
from functools import wraps
from PySide6.QtCore import QThread, SIGNAL, QMetaObject, Qt, QObject, Signal


class UIUpdateSignal(QObject):
    """Signal object for UI updates"""

    update_text = Signal(str)
    clear_image = Signal()
    load_image = Signal(str)
    show_upload_menu = Signal()


def async_action(func):
    """Decorator to run action in separate thread and automatically enable buttons"""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Check if another action is already running
        if (
            hasattr(self.main_window, "action_thread")
            and self.main_window.action_thread
            and self.main_window.action_thread.isRunning()
        ):
            print("Action is already running, skipping...")
            return

        # Disable all buttons except the current one
        if hasattr(self.main_window, "disable_other_buttons"):
            self.main_window.disable_other_buttons(self.main_window.sender())

        # Create thread to run action
        self.main_window.action_thread = ActionThread(func, self, *args, **kwargs)
        if hasattr(self.main_window, "on_action_finished"):
            self.main_window.action_thread.connect(
                SIGNAL("finished()"), self.main_window.on_action_finished
            )
        self.main_window.action_thread.start()

    return wrapper


class ActionThread(QThread):
    """Thread to run asynchronous actions"""

    def __init__(self, func, instance, *args, **kwargs):
        super().__init__()
        self.func = func
        self.instance = instance
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            # Add small delay to avoid spamming
            time.sleep(0.1)
            self.func(self.instance, *self.args, **self.kwargs)
        except Exception as e:
            print(f"Error in action: {e}")
        finally:
            self.emit(SIGNAL("finished()"))


def safe_ui_update(main_window, method_name, *args, **kwargs):
    """Safely update UI elements from a background thread using signal/slot"""
    if not hasattr(main_window, "ui_update_signal"):
        main_window.ui_update_signal = UIUpdateSignal()
        main_window.ui_update_signal.update_text.connect(main_window._set_text_to_editor)
        main_window.ui_update_signal.clear_image.connect(main_window._clear_image_safe)
        main_window.ui_update_signal.load_image.connect(main_window._load_image_to_area)
        main_window.ui_update_signal.show_upload_menu.connect(main_window._show_upload_menu)

    if method_name == "set_status_message" and args:
        # args[0]: message, args[1] (optional): status_type
        message = args[0]
        status_type = args[1] if len(args) > 1 else "info"
        main_window.set_status_message(message, status_type)
    elif method_name == "_set_text_to_editor" and args:
        main_window.ui_update_signal.update_text.emit(args[0])
    elif method_name == "_clear_image" or method_name == "_clear_image_safe":
        main_window.ui_update_signal.clear_image.emit()
    elif method_name == "_load_image_to_area" and args:
        main_window.ui_update_signal.load_image.emit(args[0])
    elif method_name == "_show_upload_menu":
        main_window.ui_update_signal.show_upload_menu.emit()
