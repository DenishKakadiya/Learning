answer = ""
score = 0
qaList = [
    ("What is full form of CPU?: ", "central processing unit"),
    ("What is full form of RAM?: ", "random access memory"),
    ("What is full form of GPU?: ", "graphic processing unit"),
    ("What is full form of PSU?: ", "power supply unit")
]

def qaChecker(obj:tuple, score) -> int:
    answer = input(obj[0] + " ")
    if (answer.lower() == obj[1]):
        print("Correct answer.")
        return 1
    else:
        score -= 1
        print("Incorrect answer.")
        return 0


#Game intro
print('Welcome to computer quiz')
playing = input("Do you want to play? : ")

if playing.lower() != "yes":
    quit()


# Stating Q&A
print("Let's start the game")

for i in range(len(qaList)):
    score += qaChecker(qaList[i],score)
    print("Your current score now is {}".format(score))

print("Your final score is",score)
