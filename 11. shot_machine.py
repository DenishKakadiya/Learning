import random

MAX_LINES = 3
MAX_AMT = 100
MIN_AMT = 0

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 8,
    "B" : 6,
    "C" : 4,
    "D" : 2
}

def check_winnings(columns, lines, amts, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* amts 
            winning_lines.append(line +1)

    return winnings, winning_lines


def get_shot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
        
    return columns

def print_shot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row])
            

def deposit():
    while True:
        amount = input("Please enter the amount you want to put in your account : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter amount greater than zero")
        else:
            print("Enter valid number")
    return amount

def get_no_of_lines():
    while True:
        lines = input(f"Please enter the number of lines to play on (1-{MAX_LINES}) : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(F"Enter line number between 1 and {MAX_LINES}")
        else:
            print("Enter valid number")
    return lines

def get_amt():
    while True:
        amount = input("Please enter the amount you want to play per line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_AMT <= amount <= MAX_AMT:
                break
            else:
                print(f"Enter amount between {MIN_AMT} and {MAX_AMT}")
        else:
            print("Enter valid number")
    return amount

def play(balance):
    lines = get_no_of_lines()
    while True:
        amt = get_amt()
        total_amt = amt*lines
        if total_amt <= balance:
            print(f"\nYou chose to play with {amt} for {lines} lines. So the total amount is :{total_amt}.\n")
            break
        else:
            print(f"Your current balance is only {balance}. Please enter the amount accordingly")

    shots = get_shot_spin(ROWS, COLS, symbol_count)
    print_shot(shots)

    winnings, winning_lines = check_winnings(shots, lines, amt, symbol_value)
    print(f"You won {winnings}.")
    print("You won on lines no.:", *winning_lines)

    return winnings - total_amt

def main():
    balance = deposit()
    while True:
        print(f"Your balance is {balance}")
        spin = input("Do you want to play more (press Enter) or quit (q): ")
        if spin == "q":
            break
        balance += play(balance) 

    print(f"You currently have {balance}")
    
if __name__ == "__main__":
    main()