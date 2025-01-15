# Minimum CMake version required
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(ChessGame VERSION 1.0)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the source files
set(SOURCES
    src/main.cpp
    src/chess/ChessGame.cpp
    src/chess/AI.cpp
    src/chess/Rules.cpp
    src/chess/Utils.cpp
    src/gui/ChessGUI.cpp
)

# Include directories for headers
include_directories(
    src/chess
    src/gui
)

# Add the executable target
add_executable(ChessGame ${SOURCES})

# Find SFML library
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# Link SFML libraries to the executable
target_link_libraries(ChessGame sfml-graphics sfml-window sfml-system)

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Copy assets to the build directory
set(ASSETS_DIR ${CMAKE_SOURCE_DIR}/assets)

add_custom_command(
    TARGET ChessGame POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${ASSETS_DIR} $<TARGET_FILE_DIR:ChessGame>/assets
)

# Install rules (optional)
install(TARGETS ChessGame DESTINATION bin)
install(DIRECTORY ${ASSETS_DIR} DESTINATION share/ChessGame/assets)
