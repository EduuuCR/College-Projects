package main;

import models.*;
import utils.*;
import java.util.Scanner;
import java.util.List;

public class HotelBookingSystem {
    private List<Room> rooms;
    private List<Booking> bookings;
    private final Scanner scanner = new Scanner(System.in);

    public HotelBookingSystem() {
        rooms = FileManager.loadRooms("assets/rooms.json");
        bookings = FileManager.loadBookings("assets/bookings.json");
    }

    public void start() {
        System.out.println("Welcome to the Hotel Booking System!");
        while (true) {
            System.out.println("\n1. Admin Login\n2. Customer Login\n3. Exit");
            int choice = InputHelper.readInt("Choose an option: ", scanner);
            switch (choice) {
                case 1 -> adminMenu();
                case 2 -> customerMenu();
                case 3 -> {
                    System.out.println("Thank you for using the system. Goodbye!");
                    FileManager.saveRooms(rooms, "assets/rooms.json");
                    FileManager.saveBookings(bookings, "assets/bookings.json");
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private void adminMenu() {
        System.out.println("\nAdmin Menu:");
        while (true) {
            System.out.println("\n1. Add Room\n2. View Rooms\n3. Remove Room\n4. Back");
            int choice = InputHelper.readInt("Choose an option: ", scanner);
            switch (choice) {
                case 1 -> addRoom();
                case 2 -> viewRooms();
                case 3 -> removeRoom();
                case 4 -> {
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private void customerMenu() {
        System.out.println("\nCustomer Menu:");
        while (true) {
            System.out.println("\n1. Search Rooms\n2. Book Room\n3. View My Booking\n4. Cancel Booking\n5. Back");
            int choice = InputHelper.readInt("Choose an option: ", scanner);
            switch (choice) {
                case 1 -> searchRooms();
                case 2 -> bookRoom();
                case 3 -> viewMyBooking();
                case 4 -> cancelBooking();
                case 5 -> {
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private void addRoom() {
        System.out.println("\nAdding a New Room:");
        int roomNumber = InputHelper.readInt("Enter Room Number: ", scanner);
        double price = InputHelper.readDouble("Enter Room Price: ", scanner);
        rooms.add(new Room(roomNumber, price, true));
        System.out.println("Room added successfully!");
    }

    private void viewRooms() {
        System.out.println("\nRoom List:");
        for (Room room : rooms) {
            System.out.println(room);
        }
    }

    private void removeRoom() {
        int roomNumber = InputHelper.readInt("Enter Room Number to Remove: ", scanner);
        rooms.removeIf(room -> room.getRoomNumber() == roomNumber);
        System.out.println("Room removed successfully!");
    }

    private void searchRooms() {
        System.out.println("\nAvailable Rooms:");
        for (Room room : rooms) {
            if (room.isAvailable()) {
                System.out.println(room);
            }
        }
    }

    private void bookRoom() {
        System.out.println("\nBooking a Room:");
        int roomNumber = InputHelper.readInt("Enter Room Number: ", scanner);
        Room room = rooms.stream()
                .filter(r -> r.getRoomNumber() == roomNumber && r.isAvailable())
                .findFirst()
                .orElse(null);
        if (room != null) {
            String customerName = InputHelper.readString("Enter Your Name: ", scanner);
            room.setAvailable(false);
            bookings.add(new Booking(customerName, room));
            System.out.println("Room booked successfully!");
        } else {
            System.out.println("Room not available!");
        }
    }

    private void viewMyBooking() {
        String customerName = InputHelper.readString("Enter Your Name: ", scanner);
        bookings.stream()
                .filter(booking -> booking.getCustomerName().equalsIgnoreCase(customerName))
                .forEach(System.out::println);
    }

    private void cancelBooking() {
        String customerName = InputHelper.readString("Enter Your Name: ", scanner);
        Booking booking = bookings.stream()
                .filter(b -> b.getCustomerName().equalsIgnoreCase(customerName))
                .findFirst()
                .orElse(null);
        if (booking != null) {
            Room room = booking.getRoom();
            room.setAvailable(true);
            bookings.remove(booking);
            System.out.println("Booking canceled successfully!");
        } else {
            System.out.println("No booking found!");
        }
    }
}
