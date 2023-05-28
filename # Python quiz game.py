# Python quiz game
# Declare all the Collections and variable we need:
#   Questions,Answers, Quit, 
# We need a Tuple of questions, a 2D tuple of options
# You need to have 15 questions
# It will also have a tuple of answers
# There will be a list of guesses so we can append our list.

# There will be these variables:
# score set 0


# Math python quiz
questions = [("What is the square root of 15: ",
             "Sum of the interior angles of a octagon: ", 
             "What is number on the top half of a fraction called: ",  
             "How many faces does a dodecehedron have: ",
             "What is the square root of 196: ",
             "What are the first five digits of pi: ",
             "Which prime number is closest to 100: ",
             "How to find the gradient of a line: ",
             "Expand (x+2)(x+6): ",
             "Expand (x-2)^2: ",
             "How to find simple interest: ",
             "How to find compound interest: ",
             "What is the most famous fratal called: ",
             "Which number has 3 significant figures: ",
             "What is this symbol called 'θ': ",)]


# 2D Tuple of options - 4 for every question as each inner 
# Tuple will have four elements
"""options = ((), this first element corresponds to the first question
            (), corresponds to 2nd question
            (), corresponds to 3rd question
            ()) corresponds to 4th question"""

options = (("A. 225", "B. 205", "C. 235", "D. 175"),
           ("A. 1420", "B. 1260", "C. 720", "D. 1080"),
           ("A. Denominator ", "B. Numerator", "C. Common divisor", "D. Common measure"),
           ("A. 10", "B. 6", "C. 12", "D. 24"),
           ("A. 12", "B. 14", "C. 16", "D. 18"),
           ("A. 3.1342  ", "B. 3.1423", "C. 3.1425", "D. 3.1415"),
           ("A. 91", "B. 99", "C. 97", "D. 93"),
           ("A. run/rise", "B y-intercept/run. ", "C. rise/run", "D. rise/y-intercept"),
           ("A. x^2 + 8x + 12", "B. x^2 + 12x + 8", "C. x^2 + 12x + 12", "D. x^2 + 12x + 4"),
           ("A. x^2 - 4x + 4", "B. x^2 - 8x + 8", "C. x^2 - 4x + 8", "D. x^2 + 8x - 4"),
           ("A. Principal / Rate x Time", "B. Principal x Rate x Time", "C. Principal / Rate / Time", "D. Principal x Rate / Time"),
           ("A. (P^R) x T", "B. (P^2)R/T", "C. P / R^T", "D. P(R)^T"),
           ("A. T-Square", "B.  Koch snowflake", "C. Menger sponge", "D. Mandelbrot set"),
           ("A. 682.82", "B. 680.2", "C. 682", "D. 680.02"),
           ("A. Omega", "B. Alpha", "C. Theta", "D. Delta"),)
            
answers = ("A", "D", "B", "C", "B", "D", "C", "C", "A", "B", "B", "D", "D", "C", "C")

guess = []

score = 0
total_questions = len(questions)

for i in range(total_questions):
    current_question = questions[i]
    print("Question", i+1, ":", current_question["question"])
    options = current_question["options"]

    # Print options
    for key, value in options.items():

        
        print(f"({key}) {value}")

    user_answer = input("Your answer (enter A, B, C, or D): ").lower()

    if user_answer == current_question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print()  # Print an empty line between questions

# Quiz summary
print("\nQuiz completed!")
print("Your score:", score, "/", total_questions)