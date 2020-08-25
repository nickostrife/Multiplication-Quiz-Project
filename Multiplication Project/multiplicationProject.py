#! python3
# Multiplication quiz python program made by myself, utilizing pyinputplus library.

""" This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:
    - If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
    - The user gets three tries to enter the correct answer before the program moves on to the next question.
    - Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.
"""

import os
import pyinputplus as pyip
import random
from queryDataMultiplication import query_all_tables as query
from insertDataMultiplication import insert_score as insert

# Todo: create function main game code here
def mainGame():
    score = 0
    number = 1    # Number of questions
    while number <= 10:
        try:
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c = pyip.inputInt("{}. {} x {} = ".format(number, a, b), timeout=8)
        except pyip.TimeoutException:
            print("8 seconds passed! Timeout!")
            c = None
        if c == (a*b):
            score += 1
        number += 1
    
    print("END OF QUESTION!")
    print("{}, Your score: {}".format(playerName, score))

    return score

# Todo: player name and score database insert

# Todo: create function to display top ten high scores form database


if __name__ == "__main__":
    # Todo: Print Welcome message, menu: 1. new game, 2. high scores, 3. exit
    while True:
        print("Python Multiplication Game!\nCreated by Nicko\n")
        playerInput = pyip.inputMenu(["New Game","High Scores","Exit"], numbered = True)

        if playerInput == "New Game":
            # Run the game
            playerName = pyip.inputStr("Input your name: ")
            userScore = mainGame()
            # Todo: Insert user score
            insert(playerName, userScore)
            input("Press Enter to continue..")

        elif playerInput == "High Scores":
            query("high_score")
            input("Press Enter to continue..")

        else:
            os._exit(1)