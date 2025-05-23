#!/bin/bash

echo "Compiling Java classes..."
mkdir -p build
javac -cp "lib/gson-2.10.1.jar:src" -d build src/main/LibrarySystem.java src/models/Book.java src/models/Member.java src/utils/FileManager.java src/utils/InputHelper.java

if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

echo "Running the program..."
java -cp "lib/gson-2.10.1.jar:build" main.LibrarySystem
