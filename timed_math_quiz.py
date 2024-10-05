import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

#problem generating function
def generate_prob():
    left = random.randrange(MIN_OPERAND,MAX_OPERAND)
    right = random.randrange(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp, answer  

generate_prob()

input("Press Enter to start!")
print("---------------------------------------")

start_time = time.time()

wrong = 0
for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_prob()

    q_start_time = time.time()
    while True:
        user_answer = input(f"Problem #{i+1} : {exp} = ")
        if (user_answer == str(answer)):
            print("Correct answer.")
            break
        else:
            print("Incorrect answer. Enter different answer.")
            wrong += 1 
    q_end_time = time.time()
    q_duration = q_end_time - q_start_time
    print(f"You took {round(q_duration,2)} sec for this question \n")


print("--------------------------------------")
end_time = time.time()
total_time = end_time - start_time
print(f"Your total time is {round(total_time,2)} sec")


