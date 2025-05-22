import models.Book;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class BookTest {

    @Test
    public void testBookCreation() {
        Book book = new Book("Test Title", "Test Author");
        assertEquals("Test Title", book.getTitle());
        assertEquals("Test Author", book.getAuthor());
        assertFalse(book.isBorrowed());
    }

    @Test
    public void testBookToString() {
        Book book = new Book("Title", "Author");
        String output = book.toString();
        assertTrue(output.contains("Title"));
        assertTrue(output.contains("Author"));
    }
}
