import main.LibrarySystem;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

public class LibrarySystemTest {

    @Test
    public void testMainRunsWithoutException() {
        assertDoesNotThrow(() -> LibrarySystem.main(new String[]{}));
    }
}
