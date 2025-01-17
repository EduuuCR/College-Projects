import org.junit.jupiter.api.*;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

// Unit tests for the Question class
public class QuestionTest {

    @Test
    public void testCorrectAnswer() {
        List<String> options = Arrays.asList("Option 1", "Option 2", "Option 3", "Option 4");
        Question question = new Question("Sample Question?", options, 2);

        assertTrue(question.isCorrect(2), "The correct answer should be identified.");
        assertFalse(question.isCorrect(1), "An incorrect answer should be identified.");
    }

    @Test
    public void testGetCorrectOption() {
        List<String> options = Arrays.asList("Option 1", "Option 2", "Option 3", "Option 4");
        Question question = new Question("Sample Question?", options, 2);

        assertEquals("Option 2", question.getCorrectOption(), "The correct option should be returned.");
    }
}
