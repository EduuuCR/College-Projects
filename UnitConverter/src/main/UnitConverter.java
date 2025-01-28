package main;

import utils.ConversionUtils;

import java.util.Scanner;

public class UnitConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Unit Converter!");
        System.out.println("Select the type of conversion:");
        System.out.println("1. Length");
        System.out.println("2. Weight");
        System.out.println("3. Temperature");
        System.out.println("4. Exit");

        int choice = 0;
        while (choice != 4) {
            System.out.print("\nEnter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character

            switch (choice) {
                case 1:
                    ConversionUtils.convertLength(scanner);
                    break;
                case 2:
                    ConversionUtils.convertWeight(scanner);
                    break;
                case 3:
                    ConversionUtils.convertTemperature(scanner);
                    break;
                case 4:
                    System.out.println("Exiting the Unit Converter. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }

        scanner.close();
    }
}
