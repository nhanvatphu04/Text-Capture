# FindTesseract.cmake
# Locates the Tesseract library
#
# This module defines the following variables:
#   Tesseract_FOUND        - True if Tesseract is found
#   Tesseract_INCLUDE_DIRS - Tesseract include directories
#   Tesseract_LIBRARIES    - Tesseract libraries
#   Tesseract_VERSION      - Tesseract version

# Common installation paths for Tesseract on Windows
set(TESSERACT_POSSIBLE_PATHS
    "C:/Users/xuan2/vcpkg/installed/x64-windows"
    "C:/Users/xuan2/AppData/Local/Programs/Tesseract-OCR"
    "C:/Program Files/Tesseract-OCR"
    "C:/Program Files (x86)/Tesseract-OCR"
    "C:/tesseract"
    "D:/Program Files/Tesseract-OCR"
    "D:/Program Files (x86)/Tesseract-OCR"
    "D:/tesseract"
    "$ENV{PROGRAMFILES}/Tesseract-OCR"
    "$ENV{ProgramFiles\(x86\)}/Tesseract-OCR"
)

# Find include directory
find_path(Tesseract_INCLUDE_DIR
    NAMES tesseract/baseapi.h
    PATHS ${TESSERACT_POSSIBLE_PATHS}
    PATH_SUFFIXES include
    DOC "Tesseract include directory"
)

# Find library
find_library(Tesseract_LIBRARY
    NAMES tesseract tesseract41 tesseract50 tesseract55
    PATHS ${TESSERACT_POSSIBLE_PATHS}
    PATH_SUFFIXES lib
    DOC "Tesseract library"
)

# Find version
if(Tesseract_INCLUDE_DIR)
    file(READ "${Tesseract_INCLUDE_DIR}/tesseract/version.h" TESSERACT_VERSION_H)
    string(REGEX MATCH "#define TESSERACT_VERSION_STR \"([0-9]+\\.[0-9]+\\.[0-9]+)\"" _ ${TESSERACT_VERSION_H})
    if(CMAKE_MATCH_1)
        set(Tesseract_VERSION ${CMAKE_MATCH_1})
    endif()
endif()

# Handle REQUIRED and QUIET arguments
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Tesseract
    REQUIRED_VARS Tesseract_LIBRARY Tesseract_INCLUDE_DIR
    VERSION_VAR Tesseract_VERSION
)

# Set output variables
if(Tesseract_FOUND)
    set(Tesseract_LIBRARIES ${Tesseract_LIBRARY})
    set(Tesseract_INCLUDE_DIRS ${Tesseract_INCLUDE_DIR})
endif()

# Mark as advanced
mark_as_advanced(Tesseract_INCLUDE_DIR Tesseract_LIBRARY) 