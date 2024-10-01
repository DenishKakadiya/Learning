#
import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    #user input and check for valid input
    user_choice = input("Enter rock/paper/scissors or 'Q' to quit : ").lower()
    if (user_choice == "q"):
        break

    if user_choice not in options:
        print("please enter a valid input")
        continue


    #generate computer choice
    comp_choice = random.choice(options)
    print("Computer selected {}".format(comp_choice))


    #check for win
    if (user_choice == comp_choice):
        print("It's a tie")
    elif (user_choice == "rock" and comp_choice == "scissors"):
        print("You won!!")
        user_wins += 1
    elif (user_choice == "paper" and comp_choice == "rock"):
        print("You won!")
        user_wins += 1
    elif (user_choice == "scissors" and comp_choice == "paper"):
        print("You won!")
        user_wins += 1
    else:
        print("Computer won!")
        comp_wins += 1


print("-----------------------------------------------")
print("Game ended.")
print(f"You won {user_wins} times and computer won {comp_wins} times")