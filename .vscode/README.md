# VS Code Setup Guide

## C++ Configuration

### 1. Copy Template
Copy `c_cpp_properties.json.template` to `c_cpp_properties.json`:
```bash
cp c_cpp_properties.json.template c_cpp_properties.json
```

### 2. Set Environment Variables

Set these environment variables in your system:

#### Windows (PowerShell)
```powershell
# OpenCV
$env:OPENCV_DIR = "D:/opencv/opencv/build"

# vcpkg
$env:VCPKG_ROOT = "C:/Users/your_username/vcpkg"

# Python
$env:PYTHON_PATH = "C:/Users/your_username/AppData/Local/Programs/Python/Python313"

# Visual Studio
$env:MSVC_PATH = "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.43.34808/bin/Hostx64/x64"
```

#### Windows (Command Prompt)
```cmd
set OPENCV_DIR=D:\opencv\opencv\build
set VCPKG_ROOT=C:\Users\your_username\vcpkg
set PYTHON_PATH=C:\Users\your_username\AppData\Local\Programs\Python\Python313
set MSVC_PATH=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.43.34808\bin\Hostx64\x64
```

### 3. Update Paths in c_cpp_properties.json

Replace the environment variables with your actual paths:

```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**",
                "D:/opencv/opencv/build/include",
                "C:/Users/your_username/vcpkg/installed/x64-windows/include",
                "C:/Users/your_username/AppData/Local/Programs/Python/Python313/Lib/site-packages/pybind11/include",
                "C:/Users/your_username/AppData/Local/Programs/Python/Python313/Include"
            ],
            "compilerPath": "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.43.34808/bin/Hostx64/x64/cl.exe"
        }
    ]
}
```

## Required Extensions

Install these VS Code extensions:

1. **C/C++** (ms-vscode.cpptools)
2. **CMake Tools** (ms-vscode.cmake-tools)
3. **Python** (ms-python.python)
4. **Qt tools** (ms-vscode.vscode-qt-tools)

## Troubleshooting

### IntelliSense Issues
- Reload VS Code after setting environment variables
- Check that all paths exist and are accessible
- Verify compiler path is correct for your Visual Studio version

### CMake Issues
- Ensure CMake is installed and in PATH
- Check that vcpkg is properly installed
- Verify OpenCV is built with the correct architecture (x64)

## Notes

- The `.vscode/` folder is ignored by git to avoid conflicts
- Each developer should have their own `c_cpp_properties.json` with their local paths
- Update this README if you add new dependencies or change the build setup 