# Quiz System

## Overview
The **Quiz System** is a simple Java-based console application that allows users to answer questions and receive scores based on their responses. It is designed to be flexible and customizable, with questions stored in a JSON file.

## Features
- Load questions from a JSON file.
- Display multiple-choice questions to the user.
- Calculate and display the final score.
- Customizable configuration via a `config.properties` file.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <QuizSystem>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd quiz-system
   ```

3. **Compile the source files:**
   ```bash
   javac -d build src/**/*.java
   ```

4. **Run the application:**
   ```bash
   java -cp build Main
   ```

## Project Structure
```
quiz-system/
├── src/
│   ├── Main.java
│   ├── QuizSystem.java
│   └── Question.java
├── assets/
│   ├── question.json
├── config.properties
├── build/
├── .gitignore
├── README.md
└── DESIGN.md
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
