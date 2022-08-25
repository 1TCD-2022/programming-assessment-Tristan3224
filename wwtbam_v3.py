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
QUESTIONS = [{"Question": "Question 1 ($100): What is the capital of the United Kingdom?",
              "Option A": "Washington D.C.",
              "Option B": "Toronto",
              "Option C": "London",
              "Option D": "Sydney"},
             {"Question": '''Question 2 ($200): Someone who wants you to behave may tell you
                   to “mind your…” which two letters?''',
              "Option A": "As and Bs",
              "Option B": "Ms and Ns",
              "Option C": "Xs and Ys",
              "Option D": "Ps and Qs"},
             {"Question": '''Question 3 ($300): In maths, what type of numbers are pi (π) and
                   Euler’s number (e)?''',
              "Option A": "Irrational",
              "Option B": "Dramatic",
              "Option C": "Hysterical",
              "Option D": "Temperamental"},
             {"Question": '''Question 4 ($500): What number was skipped in the model lineups
                   of the Apple iPhone and Microsoft Windows?''',
              "Option A": "7",
              "Option B": "8",
              "Option C": "9",
              "Option D": "11"},
             {"Question": '''Question 5 [$1,000]: In which of these decades was there NOT an
                     ongoing World War?''',
              "Option A": "1910’s",
              "Option B": "1920’s",
              "Option C": "1930’s",
              "Option D": "1940’s"},
             {"Question": '''Question 6 ($2,000): In the programming language Python, curly
                     brackets { } usually indicate what data type?''',
              "Option A": "List",
              "Option B": "Dictionary",
              "Option C": "String",
              "Option D": "Complex number"},
             {"Question": '''Question 7 ($4,000): In a standard Minecraft playthrough, what are
                     the odds of finding an End portal with all 12
                     eyes filled?''',
              "Option A": "1 in 1 billion",
              "Option B": "1 in 10 billion",
              "Option C": "1 in 100 billion",
              "Option D": "1 in 1 trillion"},
             {"Question": '''Question 8 ($8,000): In 2021, which rapper officially changed his
                     legal name to “Ye”?''',
              "Option A": "Kanye West",
              "Option B": "Eminem",
              "Option C": "Quavo",
              "Option D": "Ty Dolla $ign"},
             {"Question": '''Question 9 ($16,000): The Contiguous (or Continental) United States
                      comprises how many U.S. states?''',
              "Option A": "47",
              "Option B": "48",
              "Option C": "49",
              "Option D": "50"},
             {"Question": '''Question 10 [$32,000]: Which of these Michael Jackson hits was
                       released as a single the latest?''',
              "Option A": "Smooth Criminal",
              "Option B": "Beat It",
              "Option C": "Billie Jean",
              "Option D": "Thriller"},
             {"Question": '''Question 11 ($64,000): Commonly referred to in computing, the Unix
                       epoch (AKA “time 0”) is set to midnight UTC
                       on what day?''',
              "Option A": "January 1, 1900",
              "Option B": "January 1, 1946",
              "Option C": "January 1, 1970",
              "Option D": "January 1, 2000"},
             {"Question": '''Question 12 ($125,000): Mauna Kea, the tallest mountain in the world,
                        is not the highest point on Earth because it
                        is located how many metres below sea level?''',
              "Option A": "3,000",
              "Option B": "4,000",
              "Option C": "5,000",
              "Option D": "6,000"},
             {"Question": '''Question 13 ($250,000): In what geological period was the supercontinent
                        Pangaea formed?''',
              "Option A": "Permian",
              "Option B": "Triassic",
              "Option C": "Devonian",
              "Option D": "Jurassic"},
             {"Question": '''Question 14 ($500,000): As of August 2022, who was the last U.S. President
                        to open a Summer Olympic Games?''',
              "Option A": "George W. Bush",
              "Option B": "Bill Clinton",
              "Option C": "Ronald Reagan",
              "Option D": "Jimmy Carter"},
             {"Question": '''Question 15 {$1,000,000}: According to darts regulations, what is the
                          official distance between the front of the
                          dartboard and the back of the throw line?''',
              "Option A": "217 cm",
              "Option B": "227 cm",
              "Option C": "237 cm",
              "Option D": "247 cm"}]
# Correct answers list, with indexes that correspond to the respective questions
CORRECT_ANSWERS = ["C", "D", "A", "C", "B", "B", "D", "A", "B", "A", "C", "D", "A", "B", "C"]


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
D) {}
'''\
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
        time.sleep((loop_number + 1) / 3)   # Suspenseful pause (wait time increases with each question)
        correct_variable = 1
        print("That is the correct answer!")
    elif answer_select == "WA":
        correct_variable = -1
    elif answer_select in valid_options:
        print("Locked in.")
        time.sleep((loop_number + 1) / 3)   # Suspenseful pause (wait time increases with each question)
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
    MONEY_TREE = ["100", "200", "300", "500", "1,000", "2,000", "4,000", "8,000", "16,000", "32,000", "64,000", "125,000", "250,000", "500,000", "1,000,000"]

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
            if money_in_play == MONEY_TREE[4] or money_in_play == MONEY_TREE[9] or money_in_play == MONEY_TREE[14]:    # Safety nets
                money_safe = money_in_play
        elif user_correct_variable == -1:
            money_safe = money_in_play
            break
        elif user_correct_variable == 0:
            break

    if money_safe == MONEY_TREE[14]:
        print('''CONGRATULATIONS!
You have just won ONE MILLION DOLLARS!!! 🥳
Thank you so much for playing!''')
    else:
        print('''Your run has now ended. You have won ${}.
Thank you for playing!'''.format(money_safe))


main()
