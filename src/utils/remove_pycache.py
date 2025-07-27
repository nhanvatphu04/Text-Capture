import os
import shutil


def remove_all_pycache(root_dir=None):
    """Remove all __pycache__ directories in the given root_dir (or current directory if None)."""
    if root_dir is None:
        # Set root_dir to the project root (parent directory of this script's directory)
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "__pycache__" in dirnames:
            pycache_path = os.path.join(dirpath, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"Removed: {pycache_path}")
                count += 1
            except Exception as e:
                print(f"Failed to remove {pycache_path}: {e}")
    if count == 0:
        print("No __pycache__ directories found.")
    else:
        print(f"Removed {count} __pycache__ directories.")


if __name__ == "__main__":
    remove_all_pycache()
