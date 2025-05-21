package utils;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import models.Book;
import models.Member;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.Collections;
import java.util.List;

public class FileManager {
    private static final Gson gson = new Gson();

    public static List<Book> loadBooks(String filename) {
        try (FileReader reader = new FileReader(filename)) {
            Type listType = new TypeToken<List<Book>>() {}.getType();
            return gson.fromJson(reader, listType);
        } catch (IOException e) {
            System.out.println("Books file not found, starting with empty list.");
            return Collections.emptyList();
        }
    }

    public static void saveBooks(String filename, List<Book> books) {
        try (FileWriter writer = new FileWriter(filename)) {
            gson.toJson(books, writer);
        } catch (IOException e) {
            System.err.println("Failed to save books.");
        }
    }

    public static List<Member> loadMembers(String filename) {
        try (FileReader reader = new FileReader(filename)) {
            Type listType = new TypeToken<List<Member>>() {}.getType();
            return gson.fromJson(reader, listType);
        } catch (IOException e) {
            System.out.println("Members file not found, starting with empty list.");
            return Collections.emptyList();
        }
    }

    public static void saveMembers(String filename, List<Member> members) {
        try (FileWriter writer = new FileWriter(filename)) {
            gson.toJson(members, writer);
        } catch (IOException e) {
            System.err.println("Failed to save members.");
        }
    }
}
