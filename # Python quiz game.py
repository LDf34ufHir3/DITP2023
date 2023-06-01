# Python quiz game

#For your next assignment, you will be building a quiz game that: [f] = finished.
#   uses text based input (not a Tkinter GUI) [f]
#   asks the user 15 multiple choice questions [f]
#   uses Tuples  to store your question data (questions and answers) [f]
#   checks their answers [f]
#   keeps score [f]
#   Give out a percentage score [f]
#   Comment your code [f]
#   Show testing evidence [f]
#   asks users if they want to play again (at the end) [f]
#   Commit to Github at every stage to show version control [f]
#   Exit the program [f]


# Math python quiz
questions = [
    "What is the square root of 15: ",
    "Sum of the interior angles of an octagon: ",
    "What is the number on the top half of a fraction called: ",
    "How many faces does a dodecahedron have: ",
    "What is the square root of 196: ",
    "What are the first five digits of pi: ",
    "Which prime number is closest to 100: ",
    "How to find the gradient of a line: ",
    "Expand (x+2)(x+6): ",
    "Expand (x-2)^2: ",
    "How to find simple interest: ",
    "How to find compound interest: ",
    "What is the most famous fractal called: ",
    "Which number has 3 significant figures: ",
    "What is this symbol called 'θ': "
]

# 2D Tuple of options - 4 for every question as each inner
# Tuple will have four elements
options = (
    ("A. 225", "B. 205", "C. 235", "D. 175"),
    ("A. 1420", "B. 1260", "C. 720", "D. 1080"),
    ("A. Denominator", "B. Numerator", "C. Common divisor", "D. Common measure"),
    ("A. 10", "B. 6", "C. 12", "D. 24"),
    ("A. 12", "B. 14", "C. 16", "D. 18"),
    ("A. 3.1342", "B. 3.1423", "C. 3.1425", "D. 3.1415"),
    ("A. 91", "B. 99", "C. 97", "D. 93"),
    ("A. run/rise", "B. y-intercept/run", "C. rise/run", "D. rise/y-intercept"),
    ("A. x^2 + 8x + 12", "B. x^2 + 12x + 8", "C. x^2 + 12x + 12", "D. x^2 + 12x + 4"),
    ("A. x^2 - 4x + 4", "B. x^2 - 8x + 8", "C. x^2 - 4x + 8", "D. x^2 + 8x - 4"),
    ("A. Principal / Rate x Time", "B. Principal x Rate x Time", "C. Principal / Rate / Time", "D. Principal x Rate / Time"),
    ("A. (P^R) x T", "B. (P^2)R/T", "C. P / R^T", "D. P(R)^T"),
    ("A. T-Square", "B. Koch snowflake", "C. Menger sponge", "D. Mandelbrot set"),
    ("A. 682.82", "B. 680.2", "C. 682", "D. 680.02"),
    ("A. Omega", "B. Alpha", "C. Theta", "D. Delta")
)

answers = ("A", "D", "B", "C", "B", "D", "C", "C", "A", "B", "B", "D", "D", "C", "C")

play_again = True

while play_again:
    # Initialize variables
    score = 0
    total_questions = len(questions)

    # Quiz loop
    i = 0
    while i < total_questions:
        current_question = questions[i]
        print("Question", i+1, ":", current_question)

        # Print options
        for j in range(4):
            print(options[i][j])

        user_answer = input("Your answer (enter A, B, C, or D), or 'q' to quit the program: ").upper()

        # Option for user to quit
        if user_answer == 'Q':
            break

        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        print()  # Print an empty line between questions
        i += 1

    # Quiz summary
    print("Quiz completed!")
    print("Your score:", score, "/", total_questions)
    percentage = round((score / total_questions) * 100, 2)
    print("Percentage score:", percentage, "%")

    # Ask user if they want to play again
    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input.lower() != "yes":
        play_again = False
