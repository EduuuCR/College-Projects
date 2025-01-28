package utils;

import java.util.Scanner;

public class ConversionUtils {

    public static void convertLength(Scanner scanner) {
        System.out.println("\nLength Conversion:");
        System.out.println("1. Meters to Kilometers");
        System.out.println("2. Kilometers to Meters");
        System.out.println("3. Miles to Kilometers");
        System.out.println("4. Kilometers to Miles");

        System.out.print("Choose an option: ");
        int choice = scanner.nextInt();

        System.out.print("Enter the value to convert: ");
        double value = scanner.nextDouble();

        double result;
        switch (choice) {
            case 1 -> result = value / 1000;
            case 2 -> result = value * 1000;
            case 3 -> result = value * 1.60934;
            case 4 -> result = value / 1.60934;
            default -> {
                System.out.println("Invalid option.");
                return;
            }
        }

        System.out.printf("Converted value: %.2f\n", result);
    }

    public static void convertWeight(Scanner scanner) {
        System.out.println("\nWeight Conversion:");
        System.out.println("1. Kilograms to Pounds");
        System.out.println("2. Pounds to Kilograms");

        System.out.print("Choose an option: ");
        int choice = scanner.nextInt();

        System.out.print("Enter the value to convert: ");
        double value = scanner.nextDouble();

        double result;
        switch (choice) {
            case 1 -> result = value * 2.20462;
            case 2 -> result = value / 2.20462;
            default -> {
                System.out.println("Invalid option.");
                return;
            }
        }

        System.out.printf("Converted value: %.2f\n", result);
    }

    public static void convertTemperature(Scanner scanner) {
        System.out.println("\nTemperature Conversion:");
        System.out.println("1. Celsius to Fahrenheit");
        System.out.println("2. Fahrenheit to Celsius");

        System.out.print("Choose an option: ");
        int choice = scanner.nextInt();

        System.out.print("Enter the value to convert: ");
        double value = scanner.nextDouble();

        double result;
        switch (choice) {
            case 1 -> result = (value * 9 / 5) + 32;
            case 2 -> result = (value - 32) * 5 / 9;
            default -> {
                System.out.println("Invalid option.");
                return;
            }
        }

        System.out.printf("Converted value: %.2f\n", result);
    }
}
