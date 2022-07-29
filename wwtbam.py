'''
Filename: wwtbam.py
Author: Tristan Lim
Date: July–Aug 2022
Description: This program is meant to simulate the game show “Who Wants To Be A
Millionaire?”. The user will answer 15 trivia questions of increasing difficulty
to reach the top prize of $1,000,000.
'''


# Initialising variables
user_answer = ""
user_ready = ""
user_correct_variable = 0
VALID_ANSWER_CHOICES = ["A", "B", "C", "D", "WA"]

# Question-&-Answer Mechanism
def question_number_one(answer_select):
    # Initialising variable parameters
    QUESTION_ONE = {
    "Question": "What is the capital of the United Kingdom?",
    "Option A": "Washington D.C.",
    "Option B": "Toronto",
    "Option C": "London",
    "Option D": "Sydney"
    }
    answer_select = ""
    correct_variable = 0
    
    print('''{}
A) {}
B) {}
C) {}
D) {}'''.format(QUESTION_ONE["Question"], QUESTION_ONE["Option A"], QUESTION_ONE["Option B"], QUESTION_ONE["Option C"], QUESTION_ONE["Option D"]))
    answer_select = input("Input your answer here (type WA to walk away): ").strip().upper()
    if answer_select == "C":
        correct_variable = 1
        print("That is the correct answer!")
    elif answer_select == "WA":
        pass
    elif answer_select in VALID_ANSWER_CHOICES:
        print("I'm sorry, that is the wrong answer. The correct answer is C.")
    else:
        answer_select = input('''Invalid input. Please type A, B, C, or D to answer, and type WA to walk away (i.e. quit the game).
Input your answer here (type WA to walk away): ''').strip().upper()
    return correct_variable

# PROCEDURAL CODE
def main():
    print('''Welcome to “Who Wants To Be A Millionaire”!
You will be tested on your trivia knowledge and how well you can quiz.
If you can successfully answer 15 questions correctly, you will win the top prize… of $1,000,000!
''')
    user_ready = str(input("Type “Yes” if you're ready to begin: ").strip().title())
    while user_ready != "Yes":
        user_ready = input("Invalid input. Type “Yes” if you're ready to begin: ").strip().title()

    user_correct_variable = question_number_one(user_answer)
    if user_correct_variable == 1:
        print("Placeholder for continue.")
    else:
        pass

    print('''Your run has now ended. You have won $.
Thank you for playing!''')
        


main()
