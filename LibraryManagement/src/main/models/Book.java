package models;

public class Book {
    private String title;
    private String author;
    private boolean isBorrowed;

    public Book() {} // Required for JSON serialization

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.isBorrowed = false;
    }

    // Getters and setters (if needed)
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public boolean isBorrowed() { return isBorrowed; }

    public void setBorrowed(boolean borrowed) {
        isBorrowed = borrowed;
    }

    @Override
    public String toString() {
        return String.format("%s by %s [%s]", title, author, isBorrowed ? "Borrowed" : "Available");
    }
}
