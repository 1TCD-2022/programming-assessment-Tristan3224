'''
Filename: wwtbam.py
Author: Tristan Lim
Date: July–Aug 2022
Description: This program is meant to simulate the game show “Who Wants To Be A
Millionaire?”. The user will answer 15 trivia questions of increasing difficulty
to reach the top prize of $1,000,000.
'''


import time


# Questions list. Each question is a separate dictionary with 4 options
QUESTIONS = [{"Question": "What is the capital of the United Kingdom?",
              "Option A": "Washington D.C.",
              "Option B": "Toronto",
              "Option C": "London",
              "Option D": "Sydney" },
             {"Question": "Someone who wants you to behave may tell you to “mind your…” which two letters?",
              "Option A": "As and Bs",
              "Option B": "Ms and Ns",
              "Option C": "Xs and Ys",
              "Option D": "Ps and Qs" },
             {"Question": "In maths, what type of numbers are pi (π) and Euler’s number (e)?",
              "Option A": "Irrational",
              "Option B": "Dramatic",
              "Option C": "Hysterical",
              "Option D": "Temperamental" },
             {"Question": "What number was skipped in the model lineups of the Apple iPhone and Microsoft Windows?",
              "Option A": "7",
              "Option B": "8",
              "Option C": "9",
              "Option D": "11" },
             {"Question": "In which of these decades was there NOT an ongoing World War?",
              "Option A": "1910’s",
              "Option B": "1920’s",
              "Option C": "1930’s",
              "Option D": "1940’s" },
             {"Question": "Question 6",
              "Option A": "Option 6A",
              "Option B": "Option 6B",
              "Option C": "Option 6C",
              "Option D": "Option 6D" },
             {"Question": "Question 7",
              "Option A": "Option 7A",
              "Option B": "Option 7B",
              "Option C": "Option 7C",
              "Option D": "Option 7D" },
             {"Question": "Question 8",
              "Option A": "Option 8A",
              "Option B": "Option 8B",
              "Option C": "Option 8C",
              "Option D": "Option 8D" },
             {"Question": "Question 9",
              "Option A": "Option 9A",
              "Option B": "Option 9B",
              "Option C": "Option 9C",
              "Option D": "Option 9D" },
             {"Question": "Question 10",
              "Option A": "Option 10A",
              "Option B": "Option 10B",
              "Option C": "Option 10C",
              "Option D": "Option 10D" },
             {"Question": "Question 11",
              "Option A": "Option 11A",
              "Option B": "Option 11B",
              "Option C": "Option 11C",
              "Option D": "Option 11D" },
             {"Question": "Question 12",
              "Option A": "Option 12A",
              "Option B": "Option 12B",
              "Option C": "Option 12C",
              "Option D": "Option 12D" },
             {"Question": "Question 13",
              "Option A": "Option 13A",
              "Option B": "Option 13B",
              "Option C": "Option 13C",
              "Option D": "Option 13D" },
             {"Question": "Question 14",
              "Option A": "Option 14A",
              "Option B": "Option 14B",
              "Option C": "Option 14C",
              "Option D": "Option 14D" },
             {"Question": "Question 15",
              "Option A": "Option 15A",
              "Option B": "Option 15B",
              "Option C": "Option 15C",
              "Option D": "Option 15D" } ]
# Correct answers list, with indexes that correspond to the respective questions
CORRECT_ANSWERS = ["C", "D", "A", "C", "B", "", "", "", "", "", "", "", "", "", ""]


# Question-&-Answer Mechanism
def question_and_answer(answer_select, loop_number, valid_options):
    # Initialising variable parameters
    answer_select = ""
    correct_variable = 0

    # Print the questions in this simple format
    print('''{}
A) {}
B) {}
C) {}
D) {}'''\
# The following 5 lines extract the question and options from the dictionaries
# within the list based on the loop (i.e. question) number.
.format(QUESTIONS[loop_number].get("Question"), \
        QUESTIONS[loop_number].get("Option A"), \
        QUESTIONS[loop_number].get("Option B"), \
        QUESTIONS[loop_number].get("Option C"), \
        QUESTIONS[loop_number].get("Option D")))
    answer_select = input("Input your answer here (type WA to walk away): ").strip().upper()
    while answer_select not in valid_options:    # Input Validator
        answer_select = input('''Invalid input. Please type A, B, C, or D to answer, and type WA to walk away (i.e. quit the game).
Input your answer here (type WA to walk away): ''').strip().upper()
    

    # Now the input is checked against the correct answer of the question, which
    # is stored in a separate list but has indexes that line up with the
    # respective questions.
    if answer_select == CORRECT_ANSWERS[loop_number]:
        print("Locked in.")
        time.sleep((loop_number + 1) / 2)   # Suspenseful pause (wait time increases with each question)
        correct_variable = 1
        print("That is the correct answer!")
    elif answer_select == "WA":
        correct_variable = -1
    elif answer_select in valid_options:
        print("Locked in.")
        time.sleep((loop_number + 1) / 2)   # Suspenseful pause (wait time increases with each question)
        print("I'm sorry, that is the wrong answer. The correct answer is {}."\
              .format(CORRECT_ANSWERS[loop_number]))
    return correct_variable

# PROCEDURAL CODE
def main():
    # Initialising variables
    user_answer = ""
    user_ready = ""
    user_correct_variable = 0
    money_in_play = 0
    money_safe = 0
    VALID_ANSWER_CHOICES = ["A", "B", "C", "D", "WA"]
    MONEY_TREE = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    # Welcome Message
    print('''Welcome to “Who Wants To Be A Millionaire”!
You will be tested on your trivia knowledge and how well you can quiz.
If you can successfully answer 15 questions correctly, you will win the top
prize… of $1,000,000!
''')
    user_ready = str(input("Type “Yes” if you're ready to begin: ").strip().title())
    while user_ready != "Yes":    # Input Validator
        user_ready = input("Invalid input. Type “Yes” if you're ready to begin: ").strip().title()

    for question_number in range(15):
        user_correct_variable = question_and_answer(user_answer, question_number, VALID_ANSWER_CHOICES)
        if user_correct_variable == 1:
            money_in_play = MONEY_TREE[question_number]
            if money_in_play == MONEY_TREE[4] or money_in_play == MONEY_TREE[9]:    # Safety nets
                money_safe = money_in_play
        elif user_correct_variable == -1:
            money_safe = money_in_play
            break
        elif user_correct_variable == 0:
            break

    print('''Your run has now ended. You have won ${}.
Thank you for playing!'''.format(money_safe))
        


main()
