@echo off
echo Compiling Java classes...
javac -cp "lib\gson-2.10.1.jar;src" -d build src\main\LibrarySystem.java src\models\Book.java src\models\Member.java src\utils\FileManager.java src\utils\InputHelper.java

if %ERRORLEVEL% NEQ 0 (
    echo Compilation failed.
    exit /b 1
)

echo Running the program...
java -cp "lib\gson-2.10.1.jar;build" main.LibrarySystem
pause
