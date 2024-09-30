import random
import string

password = ""
passLen = int(input("Please provide length of password: "))
letters = string.ascii_letters
puncs = string.punctuation
nums = string.digits
comb = letters + puncs + nums
combList = ["letters", "puncs", "nums"]


# Basic generator
""" for i in range(passLen):
    password += random.choice(comb)

print("Your random password is :") """

# Basic generator using list comprehension
# password = "".join([random.choice(comb) for i in range(passLen)])

# Intermediate generator
""" for i in range(passLen):
    groupChoice = random.choice(combList)
    
    if groupChoice == "letters":
        password += random.choice(letters)
    elif groupChoice == "puncs":
        password += random.choice(puncs)
    else:
        password += random.choice(nums)
 """


# Optimized generator
combGroup = [letters, puncs, nums]
for _ in range(passLen):
    # Randomly select a character group and a character from it
    char_group = random.choice(combGroup)
    char = random.choice(char_group)
    password += char

print(password)