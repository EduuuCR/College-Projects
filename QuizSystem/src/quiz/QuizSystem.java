
// QuizSystem.java

import java.util.*;

// Core logic for the Quiz System
class QuizSystem {
    private final List<Question> questions;
    private int score;

    public QuizSystem() {
        this.questions = new ArrayList<>();
        this.score = 0;
        loadQuestions();
    }

    // Starts the quiz
    public void start() {
        System.out.println("Welcome to the Quiz System!");
        System.out.println("Answer the following questions:");

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < questions.size(); i++) {
            Question q = questions.get(i);
            System.out.printf("\nQuestion %d: %s\n", i + 1, q.getQuestionText());
            System.out.println("Options:");
            for (int j = 0; j < q.getOptions().size(); j++) {
                System.out.printf("%d. %s\n", j + 1, q.getOptions().get(j));
            }

            System.out.print("Your answer (1-4): ");
            int answer = scanner.nextInt();

            if (q.isCorrect(answer)) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong. Correct answer: " + q.getCorrectOption());
            }
        }

        System.out.printf("\nQuiz Over! Your score: %d/%d\n", score, questions.size());
    }

    // Loads questions into the system
    private void loadQuestions() {
        questions.add(new Question("What is the capital of France?", 
                Arrays.asList("Paris", "Berlin", "Madrid", "Rome"), 1));
        questions.add(new Question("Which planet is known as the Red Planet?", 
                Arrays.asList("Earth", "Mars", "Venus", "Jupiter"), 2));
        questions.add(new Question("Who wrote 'Hamlet'?", 
                Arrays.asList("Charles Dickens", "Leo Tolstoy", "William Shakespeare", "Mark Twain"), 3));
        questions.add(new Question("What is the largest mammal on Earth?", 
                Arrays.asList("Elephant", "Blue Whale", "Giraffe", "Great White Shark"), 2));
    }
}
