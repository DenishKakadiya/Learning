# App asks for number of players. During it's turn, each player can chose to either role dice or not role. if when rolling, dice value is anything other than 1, dice value is added to players total score. 
# if dice is 1, then player's that round's point collection is reset to zero and next player's turn comes. Game ends when a player reaches 50 points. 

import random
player_score = 0
max_score = 50

while True:
    player_num = input("Enter number of player (2-4) :")
    if(player_num.isdigit()):
        player_num = int(player_num)
        if(1 < player_num < 5):
            break
        else:
            print("Enter a valid number between 2 to 4 players")
    else:
        print("Please enter a digit")

player_score = [0 for i in range(player_num)]
print(player_score)
    
while max(player_score) < max_score:
    for player_idx in range(player_num): 
        print(f"\n\nNow, it's turn for player no. {player_idx +1}")
        print("Your current total score is", player_score[player_idx])
        current_score = 0

        while True:
            player_choice = input("Do you want to roll the dice? (Yes/No) : ").lower()
            if (player_choice not in ["yes", "no"]):
                print("please enter a valid input")
                continue
            elif (player_choice == "no"):
                print(f"You chose not to roll dice again. \nYou score for this round is {current_score}")
                break
            
            dice_value = random.randrange(1,7,1)

            if (dice_value == 1):
                current_score = 0
                print(f"Dice number is {dice_value}. \nYour score is reset back to zero")
                break
            else:
                print(f"Dice number is {dice_value}")
                current_score += dice_value
                print(f"your new score is {current_score}")
        
        player_score[player_idx] += current_score
        print("Your current total score is", player_score[player_idx])

max_score = max(player_score)
winner_index = player_score.index(max_score)
print("\n\n\nPlayer number", winner_index + 1, "wom with the score of", max_score, "\n\n")