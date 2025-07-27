#!/usr/bin/env python3
"""
Build script for C++ OCR module
"""

import os
import sys
import subprocess
import platform
import glob
from pathlib import Path


def find_msvc_compiler():
    """Find MSVC compiler on Windows"""
    print("Looking for MSVC compiler...")
    
    # Check if we're in a Visual Studio Developer Command Prompt
    if 'VCINSTALLDIR' in os.environ:
        print("✓ Visual Studio environment detected")
        return True
    
    # Try to find Visual Studio installations
    vs_paths = [
        "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files (x86)/Microsoft Visual Studio/2019/Professional/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files/Microsoft Visual Studio/2022/Professional/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files/Microsoft Visual Studio/2022/Enterprise/VC/Auxiliary/Build/vcvars64.bat",
    ]
    
    for vs_path in vs_paths:
        if os.path.exists(vs_path):
            print(f"✓ Visual Studio found at: {vs_path}")
            return True
    
    # Try to find cl.exe in PATH
    try:
        result = subprocess.run(['cl'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ MSVC compiler (cl.exe) found in PATH")
            return True
    except FileNotFoundError:
        pass
    
    # Try to find cl.exe in common locations
    cl_paths = glob.glob("C:/Program Files*/Microsoft Visual Studio/*/*/VC/Tools/MSVC/*/bin/Hostx64/x64/cl.exe")
    if cl_paths:
        print(f"✓ MSVC compiler found at: {cl_paths[0]}")
        return True
    
    print("✗ MSVC compiler not found")
    return False


def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    # Check CMake
    try:
        result = subprocess.run(['cmake', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ CMake found")
        else:
            print("✗ CMake not found")
            return False
    except FileNotFoundError:
        print("✗ CMake not found")
        return False
    
    # Check C++ compiler
    if platform.system() == "Windows":
        if not find_msvc_compiler():
            print("\nMSVC compiler not found. You can:")
            print("1. Install Visual Studio 2019/2022 with C++ workload")
            print("2. Run this script from a Visual Studio Developer Command Prompt")
            print("3. Use MinGW-w64 as an alternative")
            return False
    else:
        try:
            result = subprocess.run(['g++', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ GCC compiler found")
            else:
                print("✗ GCC compiler not found")
                return False
        except FileNotFoundError:
            print("✗ GCC compiler not found")
            return False
    
    return True


def find_opencv():
    """Find OpenCV installation"""
    print("Looking for OpenCV...")
    
    # Try to find OpenCV using pkg-config (Linux/macOS)
    if platform.system() != "Windows":
        try:
            result = subprocess.run(['pkg-config', '--modversion', 'opencv4'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✓ OpenCV found: {result.stdout.strip()}")
                return True
        except FileNotFoundError:
            pass
    
    # Try to find OpenCV in common locations
    opencv_paths = [
        "/usr/local/include/opencv4",
        "/usr/include/opencv4",
        "C:/opencv/build/include",
        "C:/Program Files/opencv/build/include",
        "C:/opencv/build/x64/vc15/include",
        "C:/opencv/build/x64/vc16/include",
        "C:/Program Files/opencv/build/x64/vc15/include",
        "C:/Program Files/opencv/build/x64/vc16/include"
    ]
    
    for path in opencv_paths:
        if os.path.exists(path):
            print(f"✓ OpenCV found at: {path}")
            return True
    
    # Try to find OpenCV using Python
    try:
        import cv2
        print(f"✓ OpenCV found via Python: {cv2.__version__}")
        return True
    except ImportError:
        pass
    
    print("✗ OpenCV not found")
    return False


def find_tesseract():
    """Find Tesseract installation"""
    print("Looking for Tesseract...")
    
    # Try to find Tesseract using pkg-config (Linux/macOS)
    if platform.system() != "Windows":
        try:
            result = subprocess.run(['pkg-config', '--modversion', 'tesseract'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✓ Tesseract found: {result.stdout.strip()}")
                return True
        except FileNotFoundError:
            pass
    
    # Try to find Tesseract in common locations
    tesseract_paths = [
        "/usr/local/include/tesseract",
        "/usr/include/tesseract",
        "C:/Program Files/Tesseract-OCR/include/tesseract",
        "C:/tesseract/include/tesseract",
        "C:/Program Files (x86)/Tesseract-OCR/include/tesseract"
    ]
    
    for path in tesseract_paths:
        if os.path.exists(path):
            print(f"✓ Tesseract found at: {path}")
            return True
    
    # Try to find tesseract executable
    try:
        result = subprocess.run(['tesseract', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Tesseract executable found")
            return True
    except FileNotFoundError:
        pass
    
    print("✗ Tesseract not found")
    return False


def setup_vs_environment():
    """Setup Visual Studio environment if needed"""
    if platform.system() != "Windows" or 'VCINSTALLDIR' in os.environ:
        return True
    
    # Try to find and run vcvars64.bat
    vs_paths = [
        "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files (x86)/Microsoft Visual Studio/2019/Professional/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files/Microsoft Visual Studio/2022/Professional/VC/Auxiliary/Build/vcvars64.bat",
        "C:/Program Files/Microsoft Visual Studio/2022/Enterprise/VC/Auxiliary/Build/vcvars64.bat",
    ]
    
    for vs_path in vs_paths:
        if os.path.exists(vs_path):
            print(f"Setting up Visual Studio environment from: {vs_path}")
            # Note: This would require running the script in a cmd shell that has run vcvars64.bat
            # For now, we'll just inform the user
            print("Please run this script from a Visual Studio Developer Command Prompt")
            print(f"Or run: \"{vs_path}\" && python build_cpp.py")
            return False
    
    return True


def build_cpp_module():
    """Build C++ OCR module"""
    print("Building C++ OCR module...")
    
    # Get current directory
    current_dir = Path(__file__).parent
    cpp_dir = current_dir / "src" / "ocr" / "cpp"
    build_dir = cpp_dir / "build"
    
    # Create build directory
    build_dir.mkdir(exist_ok=True)
    
    # Change to build directory
    original_dir = os.getcwd()
    os.chdir(build_dir)
    
    try:
        # Configure with CMake
        print("Configuring with CMake...")
        cmake_cmd = [
            'cmake', '..',
            '-DCMAKE_BUILD_TYPE=Release'
        ]
        
        if platform.system() == "Windows":
            # Try different Visual Studio generators
            generators = [
                'Visual Studio 17 2022',
                'Visual Studio 16 2019',
                'Visual Studio 15 2017'
            ]
            
            cmake_success = False
            for generator in generators:
                try:
                    test_cmd = cmake_cmd + ['-G', generator]
                    result = subprocess.run(test_cmd, capture_output=True, text=True, timeout=30)
                    if result.returncode == 0:
                        cmake_cmd = test_cmd
                        cmake_success = True
                        print(f"✓ Using CMake generator: {generator}")
                        break
                except (subprocess.TimeoutExpired, FileNotFoundError):
                    continue
            
            if not cmake_success:
                print("✗ Failed to configure CMake with any Visual Studio generator")
                return False
        
        result = subprocess.run(cmake_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"✗ CMake configuration failed: {result.stderr}")
            return False
        
        print("✓ CMake configuration successful")
        
        # Build
        print("Building...")
        if platform.system() == "Windows":
            build_cmd = ['cmake', '--build', '.', '--config', 'Release']
        else:
            build_cmd = ['make', '-j4']
        
        result = subprocess.run(build_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"✗ Build failed: {result.stderr}")
            return False
        
        print("✓ Build successful")
        
        # Check if the module was created
        module_path = current_dir / "cpp_ocr"
        if platform.system() == "Windows":
            module_path = module_path.with_suffix('.pyd')
        else:
            module_path = module_path.with_suffix('.so')
        
        if module_path.exists():
            print(f"✓ C++ module created: {module_path}")
            return True
        else:
            print(f"✗ C++ module not found at: {module_path}")
            return False
    
    finally:
        # Restore original directory
        os.chdir(original_dir)


def install_dependencies():
    """Install Python dependencies"""
    print("Installing Python dependencies...")
    
    requirements = [
        'pybind11',
        'opencv-python',
        'pytesseract',
        'easyocr',
        'pillow',
        'numpy'
    ]
    
    for package in requirements:
        print(f"Installing {package}...")
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {package} installed")
        else:
            print(f"✗ Failed to install {package}: {result.stderr}")


def main():
    """Main build function"""
    print("TextCapture C++ OCR Module Builder")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        print("\nPlease install missing dependencies:")
        print("- CMake: https://cmake.org/download/")
        print("- Visual Studio 2019/2022 with C++ workload")
        print("- OpenCV: https://opencv.org/releases/")
        print("- Tesseract: https://github.com/tesseract-ocr/tesseract")
        print("\nFor Windows users:")
        print("1. Install Visual Studio 2019/2022 Community Edition")
        print("2. During installation, select 'Desktop development with C++' workload")
        print("3. Run this script from a Visual Studio Developer Command Prompt")
        return False
    
    # Setup Visual Studio environment if needed
    if not setup_vs_environment():
        return False
    
    # Find libraries
    opencv_found = find_opencv()
    tesseract_found = find_tesseract()
    
    if not opencv_found:
        print("\nOpenCV not found. You can:")
        print("1. Install OpenCV from: https://opencv.org/releases/")
        print("2. Use Python OpenCV: pip install opencv-python")
        print("3. Continue without C++ OpenCV (will use Python fallback)")
        
        response = input("Continue without OpenCV? (y/n): ").lower().strip()
        if response != 'y':
            return False
    
    if not tesseract_found:
        print("\nTesseract not found. You can:")
        print("1. Install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("2. Continue without C++ Tesseract (will use Python fallback)")
        
        response = input("Continue without Tesseract? (y/n): ").lower().strip()
        if response != 'y':
            return False
    
    # Install Python dependencies
    install_dependencies()
    
    # Build C++ module
    if build_cpp_module():
        print("\n✓ C++ OCR module built successfully!")
        print("You can now use the C++ implementation for better performance.")
        return True
    else:
        print("\n✗ Failed to build C++ OCR module")
        print("The application will fall back to Python implementation.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 