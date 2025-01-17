# Design Document: Quiz System

## Purpose
This document outlines the design and architecture of the Quiz System application.

## Modules
### 1. Main
- Entry point for the application.
- Initializes the `QuizSystem` and starts the quiz.

### 2. QuizSystem
- Core logic of the application.
- Responsibilities:
  - Load questions from `question.json`.
  - Display questions and options to the user.
  - Validate user responses and calculate scores.

### 3. Question
- Represents a single quiz question.
- Encapsulates question text, options, and the correct answer index.
- Provides methods to validate answers and retrieve the correct option.

## Configuration
- The application reads its configuration from `config.properties`. This allows customization of:
  - Application title and version.
  - Location of the questions file.

## Data Storage
- Questions are stored in `question.json` in the following format:
  ```json
  [
      {
          "question": "What is the capital of France?",
          "options": ["Paris", "Berlin", "Madrid", "Rome"],
          "correctOption": 1
      }
  ]
  ```

## Future Enhancements
- Add support for multiple languages.
- Implement a graphical user interface.
- Add a timer for each question.
