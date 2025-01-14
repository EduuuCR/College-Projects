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

# Add the header files
set(HEADERS
    src/chess/ChessGame.h
    src/chess/AI.h
    src/chess/Rules.h
    src/chess/Utils.h
    src/gui/ChessGUI.h
)

# Add the executable target
add_executable(ChessGame ${SOURCES} ${HEADERS})

# Find SFML library
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# Link SFML libraries to the executable
target_link_libraries(ChessGame sfml-graphics sfml-window sfml-system)

# Copy assets to the build directory (optional)
add_custom_command(
    TARGET ChessGame POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${CMAKE_SOURCE_DIR}/assets $<TARGET_FILE_DIR:ChessGame>/assets
)
