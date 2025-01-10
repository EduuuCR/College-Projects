import java.util.ArrayList;
import java.util.Scanner;

// Class for Product
class Product {
    private int id;
    private String name;
    private double price;

    public Product(int id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Name: " + name + ", Price: $" + price;
    }
}

// Class for Shopping Cart
class ShoppingCart {
    private ArrayList<Product> cart;

    public ShoppingCart() {
        this.cart = new ArrayList<>();
    }

    public void addProduct(Product product) {
        cart.add(product);
        System.out.println(product.getName() + " added to the cart.");
    }

    public void removeProduct(int productId) {
        for (Product product : cart) {
            if (product.getId() == productId) {
                cart.remove(product);
                System.out.println(product.getName() + " removed from the cart.");
                return;
            }
        }
        System.out.println("Product with ID " + productId + " not found in the cart.");
    }

    public void viewCart() {
        if (cart.isEmpty()) {
            System.out.println("Your cart is empty.");
        } else {
            System.out.println("Your cart:");
            for (Product product : cart) {
                System.out.println(product);
            }
        }
    }

    public void checkout() {
        if (cart.isEmpty()) {
            System.out.println("Your cart is empty. Add products before checkout.");
        } else {
            double total = 0;
            System.out.println("Checkout details:");
            for (Product product : cart) {
                System.out.println(product);
                total += product.getPrice();
            }
            System.out.println("Total: $" + total);
            cart.clear();
            System.out.println("Thank you for shopping with us!");
        }
    }
}

// Main class
public class EcommerceSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Sample products
        ArrayList<Product> products = new ArrayList<>();
        products.add(new Product(1, "Laptop", 800.00));
        products.add(new Product(2, "Smartphone", 500.00));
        products.add(new Product(3, "Headphones", 50.00));
        products.add(new Product(4, "Keyboard", 30.00));

        ShoppingCart cart = new ShoppingCart();
        int choice;

        System.out.println("Welcome to the E-commerce System!");

        do {
            System.out.println("\nMenu:");
            System.out.println("1. View Products");
            System.out.println("2. Add Product to Cart");
            System.out.println("3. Remove Product from Cart");
            System.out.println("4. View Cart");
            System.out.println("5. Checkout");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("\nAvailable Products:");
                    for (Product product : products) {
                        System.out.println(product);
                    }
                    break;
                case 2:
                    System.out.print("Enter the product ID to add to the cart: ");
                    int addId = scanner.nextInt();
                    boolean productFound = false;
                    for (Product product : products) {
                        if (product.getId() == addId) {
                            cart.addProduct(product);
                            productFound = true;
                            break;
                        }
                    }
                    if (!productFound) {
                        System.out.println("Product with ID " + addId + " not found.");
                    }
                    break;
                case 3:
                    System.out.print("Enter the product ID to remove from the cart: ");
                    int removeId = scanner.nextInt();
                    cart.removeProduct(removeId);
                    break;
                case 4:
                    cart.viewCart();
                    break;
                case 5:
                    cart.checkout();
                    break;
                case 6:
                    System.out.println("Thank you for using the E-commerce System. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 6);

        scanner.close();
    }
}
