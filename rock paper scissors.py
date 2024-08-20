#importing
import random

#establish game loop
playing = True

while playing == True:
    #choosing computer move
    list = ["rock", "paper", "scissors"]
    cpuThrow = random.choice(list)

    #choosing user move
    inp = input("Choose rock, paper, or scissors by pressing 'r', 'p', or 's'.\n")

    choosing = True

    while choosing:
        if inp == 'r':
            userThrow = "rock"
            choosing = False
        elif inp == 'p':
            userThrow = "paper"
            choosing = False
        elif inp == 's':
            userThrow = "scissors"
            choosing = False
        else:
            inp = input("Choose rock, paper, or scissors by pressing 'r', 'p', or 's'.\n")

    #printing results
    print(f"You chose {userThrow}. The computer chose {cpuThrow}.")

    if userThrow == cpuThrow:
        print("You tied!\n")
    elif (userThrow == "scissors" and cpuThrow == "rock") or (userThrow == "rock" and cpuThrow == "paper") or (userThrow == "paper" and cpuThrow == "scissors"):
        print("You lost!\n")
    else:
        print("You won!\n")
    
    #play again loop
    playAgain = input("Would you like to play again? Press 'y' or 'n'.\n")
    playAgainQ = True

    while playAgainQ:
        if playAgain == 'y':
            playing = True
            playAgainQ = False
        elif playAgain == 'n':
            playing = False
            playAgainQ = False
        else:
            playAgain = input("Would you like to play again? Press 'y' or 'n'.\n")