package models;

public class Room {
    private int roomNumber;
    private double price;
    private boolean available;

    // Constructor
    public Room(int roomNumber, double price, boolean available) {
        this.roomNumber = roomNumber;
        this.price = price;
        this.available = available;
    }

    // Getters and Setters
    public int getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }

    @Override
    public String toString() {
        return "Room{" +
                "roomNumber=" + roomNumber +
                ", price=" + price +
                ", available=" + (available ? "Yes" : "No") +
                '}';
    }
}
