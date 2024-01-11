import sys
import random

from enum import Enum


"""
* we will learn how to take input from the user
* via building a simple Rock Paper Scissors game.
"""


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("-------------------------------")
playerChoice = input(
    "Enter ....\n 1 for Rock \n 2 for Paper \n 3 for Scissor\n 4 for Exit the Game\n\n"
)

player = int(playerChoice)
# computerChoice = random.randint(1, 3)

while True:
    if player < 1 or player > 4:
        print("invalid Choice")
        sys.exit("You Must Enter 1,2 or 3")

    if player == 4:
        sys.exit("I Hope you Enjoyed the Game")

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    print("-------------------------------")

    print(
        "| You Choose : ".ljust(20, ".")
        + str(RPS(player)).replace("RPS.", "")
        + "    |"
    )
    print(
        "| Python Choose : ".ljust(20, ".")
        + str(RPS(computer)).replace("RPS.", "")
        + "    |"
    )

    print("-------------------------------")

    if player == 1 & computer == 3:
        print("You Win 🎉 🎉 🥳")
    elif player == 2 & computer == 1:
        print("You Win 🎉 🎉 🥳")
    elif player == 3 & computer == 2:
        print("You Win 🎉 🎉 🥳")
    elif player == computer:
        print("It's a Tie 😲 😲 😲")
    else:
        print("You Lose 😔 😔 😔")

    playerChoice = input(
        "Enter ....\n 1 for Rock \n 2 for Paper \n 3 for Scissor\n 4 for Exit the Game\n\n"
    )

    player = int(playerChoice)


print()
