
// Question.java

import java.util.*;

// Represents a single quiz question
class Question {
    private final String questionText;
    private final List<String> options;
    private final int correctOptionIndex;

    public Question(String questionText, List<String> options, int correctOptionIndex) {
        this.questionText = questionText;
        this.options = options;
        this.correctOptionIndex = correctOptionIndex - 1; // Convert to zero-based index
    }

    public String getQuestionText() {
        return questionText;
    }

    public List<String> getOptions() {
        return options;
    }

    public boolean isCorrect(int answer) {
        return answer - 1 == correctOptionIndex; // Convert to zero-based index
    }

    public String getCorrectOption() {
        return options.get(correctOptionIndex);
    }
}
