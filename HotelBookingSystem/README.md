# Hotel Booking System

A Java-based hotel booking system that allows users to manage rooms, create bookings, and view existing reservations.

## Features

- Manage hotel rooms with attributes like room number, price, and availability.
- Create bookings for available rooms.
- View and save all booking information.
- Data persistence using JSON files.

## Directory Structure

hotel-booking-system/
├── src/
│   ├── main/
│   │   ├── Main.java
│   │   └── HotelBookingSystem.java
│   ├── models/
│   │   ├── Room.java
│   │   ├── Booking.java
│   ├── utils/
│   │   ├── InputHelper.java
│   │   └── FileManager.java
├── assets/
│   ├── rooms.json
│   ├── bookings.json
├── .gitignore
├── README.md



## Prerequisites

- Java Development Kit (JDK) 17 or later.
- [Gson Library](https://github.com/google/gson) for JSON handling.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/EduuuCR/HotelBookingSystem.git


2. Add the gson.jar file to the lib/ directory.

3. Compile the project and Run:
```bash
 javac -cp lib/gson.jar src/**/*.java

 java -cp lib/gson.jar:src main.Main



