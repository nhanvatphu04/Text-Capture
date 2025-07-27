#!/usr/bin/env python3
"""
Script to compile Qt resources (.qrc) to Python module
"""

import os
import sys
import subprocess
import shutil

def get_project_root():
    """Get the project root directory"""
    # If running from test directory, go up one level
    current_dir = os.getcwd()
    if os.path.basename(current_dir) == 'test':
        return os.path.dirname(current_dir)
    return current_dir

def check_pyside6_rcc():
    """Check if pyside6-rcc is available"""
    try:
        result = subprocess.run(['pyside6-rcc', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def check_pyrcc6():
    """Check if pyrcc6 is available"""
    try:
        result = subprocess.run(['pyrcc6', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def compile_resources():
    """Compile resources.qrc to src/resources_rc.py"""
    
    project_root = get_project_root()
    resources_qrc = os.path.join(project_root, 'resources.qrc')
    output_file = os.path.join(project_root, 'src', 'resources_rc.py')
    
    # Check if resources.qrc exists
    if not os.path.exists(resources_qrc):
        print(f"Error: resources.qrc not found at {resources_qrc}")
        return False
    
    # Ensure src directory exists
    src_dir = os.path.join(project_root, 'src')
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
        print(f"📁 Created src directory: {src_dir}")
    
    print(f"📁 Project root: {project_root}")
    print(f"📄 Input file: {resources_qrc}")
    print(f"📄 Output file: {output_file}")
    
    # Try pyside6-rcc first
    if check_pyside6_rcc():
        print("Using pyside6-rcc...")
        try:
            result = subprocess.run([
                'pyside6-rcc', 
                resources_qrc, 
                '-o', output_file
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Successfully compiled resources with pyside6-rcc")
                return True
            else:
                print(f"❌ Error with pyside6-rcc: {result.stderr}")
        except Exception as e:
            print(f"❌ Exception with pyside6-rcc: {e}")
    
    # Try pyrcc6 as fallback
    elif check_pyrcc6():
        print("Using pyrcc6...")
        try:
            result = subprocess.run([
                'pyrcc6', 
                resources_qrc, 
                '-o', output_file
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Successfully compiled resources with pyrcc6")
                return True
            else:
                print(f"❌ Error with pyrcc6: {result.stderr}")
        except Exception as e:
            print(f"❌ Exception with pyrcc6: {e}")
    
    else:
        print("❌ Neither pyside6-rcc nor pyrcc6 found!")
        print("Please install PySide6 or PyQt6:")
        print("  pip install PySide6")
        print("  # or")
        print("  pip install PyQt6")
        return False
    
    return False

def verify_compiled_file():
    """Verify that src/resources_rc.py was created and is valid"""
    project_root = get_project_root()
    resources_rc_path = os.path.join(project_root, 'src', 'resources_rc.py')
    
    if not os.path.exists(resources_rc_path):
        print(f"❌ src/resources_rc.py was not created at {resources_rc_path}")
        return False
    
    try:
        # Add src directory to Python path
        src_dir = os.path.join(project_root, 'src')
        if src_dir not in sys.path:
            sys.path.insert(0, src_dir)
        
        # Try to import the compiled module
        import resources_rc
        print("✅ src/resources_rc.py is valid and can be imported")
        return True
    except Exception as e:
        print(f"❌ Error importing src/resources_rc.py: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Compiling Qt Resources...")
    print("=" * 40)
    
    # Compile resources
    if compile_resources():
        # Verify the result
        if verify_compiled_file():
            print("\n🎉 Resources compiled successfully!")
            print("You can now use resources in your application.")
            print("\nExample usage:")
            print("  from src import resources_rc")
            print("  # Then use QFile(':/style.qss') to access resources")
        else:
            print("\n⚠️  Resources compiled but verification failed!")
    else:
        print("\n❌ Failed to compile resources!")
        sys.exit(1)

if __name__ == "__main__":
    main() 