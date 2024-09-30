# App asks user to guess a number and based on guessed number will tell whether it's high or low untill user guess correct number. Then App will give number of guesses.

import random

rand_num = random.randint(0, 100)
guess_count = 0

while True:
    guess_num = input("Guess the number:")
    guess_count += 1

    #check for valid input
    if (guess_num.isdigit()):
        guess_num = int(guess_num)
        if(guess_num <= 0):
            print("Please enter a positive number")
            guess_count -=1
            continue
    else:
        print("Please enter a valid number")
        guess_count -= 1
        continue
    
    #check input number with random number
    if (guess_num > rand_num):
        print("Guessed number is too big. Try smaller one")
    elif (guess_num < rand_num):
        print("Guessed number is too small. Try bigger one")
    else:
        break

print("--------------------------------")
print("You guessed the number correctly")
print("it took you {} trys to guess it".format(guess_count))



