package utils;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import models.Booking;
import models.Room;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class FileManager {
    private static final Gson gson = new Gson();

    // Loads room data from a JSON file
    public static List<Room> loadRooms(String filePath) {
        try (FileReader reader = new FileReader(filePath)) {
            Type roomListType = new TypeToken<List<Room>>() {}.getType();
            return gson.fromJson(reader, roomListType);
        } catch (IOException e) {
            System.out.println("Error loading rooms: " + e.getMessage());
            return new ArrayList<>(); // Return an empty list if the file doesn't exist
        }
    }

    // Saves room data to a JSON file
    public static void saveRooms(List<Room> rooms, String filePath) {
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(rooms, writer);
            System.out.println("Rooms saved successfully.");
        } catch (IOException e) {
            System.out.println("Error saving rooms: " + e.getMessage());
        }
    }

    // Loads booking data from a JSON file
    public static List<Booking> loadBookings(String filePath) {
        try (FileReader reader = new FileReader(filePath)) {
            Type bookingListType = new TypeToken<List<Booking>>() {}.getType();
            return gson.fromJson(reader, bookingListType);
        } catch (IOException e) {
            System.out.println("Error loading bookings: " + e.getMessage());
            return new ArrayList<>(); // Return an empty list if the file doesn't exist
        }
    }

    // Saves booking data to a JSON file
    public static void saveBookings(List<Booking> bookings, String filePath) {
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(bookings, writer);
            System.out.println("Bookings saved successfully.");
        } catch (IOException e) {
            System.out.println("Error saving bookings: " + e.getMessage());
        }
    }
}
