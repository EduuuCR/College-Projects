package models;

public class Booking {
    private String customerName;
    private Room room;

    // Constructor
    public Booking(String customerName, Room room) {
        this.customerName = customerName;
        this.room = room;
    }

    // Getters and Setters
    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }

    @Override
    public String toString() {
        return "Booking{" +
                "customerName='" + customerName + '\'' +
                ", room=" + room +
                '}';
    }
}
