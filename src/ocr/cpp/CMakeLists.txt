cmake_minimum_required(VERSION 3.16)
project(TextCaptureOCR)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(OpenCV REQUIRED)
find_package(Tesseract REQUIRED)
find_package(pybind11 REQUIRED)

# Include directories
include_directories(${OpenCV_INCLUDE_DIRS})
include_directories(${Tesseract_INCLUDE_DIRS})

# Source files
set(SOURCES
    ocr_engine.cpp
    ocr_engine.h
    ocr_engine.cpp
)

# Create shared library
pybind11_add_module(cpp_ocr ${SOURCES})

# Link libraries
target_link_libraries(cpp_ocr 
    ${OpenCV_LIBS}
    ${Tesseract_LIBRARIES}
)

# Set output directory
set_target_properties(cpp_ocr PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/../..
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/../..
)

# Compiler specific settings
if(MSVC)
    target_compile_options(cpp_ocr PRIVATE /W4)
else()
    target_compile_options(cpp_ocr PRIVATE -Wall -Wextra -O3)
endif()

# Installation
install(TARGETS cpp_ocr
    LIBRARY DESTINATION ${CMAKE_SOURCE_DIR}/../..
) 