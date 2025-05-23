
---

### ✅ `DESIGN.md`

```markdown
# 🧠 Design Document — Simple Library Management System

## 🎯 Objective

Design and implement a lightweight, command-line library system for educational purposes. It should be easy to extend and should persist data using JSON.

---

## 📐 Architecture Overview

This is a **modular Java application** with clear separation of concerns:

- `models/`: Data objects (`Book`, `Member`)
- `utils/`: Utility classes for file I/O and input validation
- `main/`: Application entry point and core logic
- `data/`: JSON storage for persistent data
- `test/`: Unit testing for core functionality

---

## 🧱 Classes

### 📘 `Book`

- Fields: `title`, `author`, `borrowed`
- Methods: `getters/setters`, `toString`

### 👤 `Member`

- Field: `name`
- Methods: `getName`, `toString`

### 🏗 `FileManager`

- Uses **Gson** to load/save JSON data
- Handles missing files gracefully

### 🎮 `LibrarySystem`

- Main application logic
- Menu-driven interface for user interaction

---

## 💾 Data Storage

- `books.json`: Stores an array of book objects
- `members.json`: Stores an array of registered members
- Format: JSON (parsed using Gson)

---

## 🧪 Testing

- Unit tests for `Book`, `Member`, and `LibrarySystem`
- Uses JUnit 5
- Ensures data integrity and program stability

---

## 🔄 Extensibility

Future features could include:

- Due dates and overdue tracking
- Categories or genres
- Graphical user interface (Swing or JavaFX)
- Admin/guest roles

---

## ✅ Dependencies

- Gson 2.10.1 (JSON serialization/deserialization)
- JUnit 5 (unit testing)

---

## 🎓 Educational Value

This project demonstrates:
- Object-oriented programming
- File I/O and JSON in Java
- Clean code architecture
- Writing maintainable, testable code

---

