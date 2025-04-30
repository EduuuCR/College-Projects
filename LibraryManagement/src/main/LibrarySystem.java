package main;

import models.Book;
import models.Member;
import utils.FileManager;
import utils.InputHelper;

import java.util.*;

public class LibrarySystem {
    private static final Scanner scanner = new Scanner(System.in);
    private static List<Book> books = new ArrayList<>();
    private static List<Member> members = new ArrayList<>();

    public static void main(String[] args) {
        books = FileManager.loadBooks("data/books.json");
        members = FileManager.loadMembers("data/members.json");

        while (true) {
            System.out.println("\n--- Library Management System ---");
            System.out.println("1. View Books");
            System.out.println("2. Add Book");
            System.out.println("3. Register Member");
            System.out.println("4. View Members");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = InputHelper.readInt(scanner);

            switch (choice) {
                case 1 -> viewBooks();
                case 2 -> addBook();
                case 3 -> registerMember();
                case 4 -> viewMembers();
                case 5 -> {
                    FileManager.saveBooks("data/books.json", books);
                    FileManager.saveMembers("data/members.json", members);
                    System.out.println("Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid choice.");
            }
        }
    }

    private static void viewBooks() {
        if (books.isEmpty()) {
            System.out.println("No books available.");
        } else {
            books.forEach(System.out::println);
        }
    }

    private static void addBook() {
        System.out.print("Enter title: ");
        String title = scanner.nextLine();
        System.out.print("Enter author: ");
        String author = scanner.nextLine();
        books.add(new Book(title, author));
        System.out.println("Book added!");
    }

    private static void registerMember() {
        System.out.print("Enter member name: ");
        String name = scanner.nextLine();
        members.add(new Member(name));
        System.out.println("Member registered!");
    }

    private static void viewMembers() {
        if (members.isEmpty()) {
            System.out.println("No members registered.");
        } else {
            members.forEach(System.out::println);
        }
    }
}
