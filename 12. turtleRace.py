import turtle

WIDTH, HEIGHT = 500, 500

def get_no_of_racers():
    while True:
        racers = input("Enter number of turtles to race (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Please enter number higher than 2")
        else:
            print("please enter a valid number.")

def main():
    racers = get_no_of_racers()
    print(racers)

    screen = turtle.Screen()
    screen.screensize(WIDTH, HEIGHT)

if __name__ == "__main__":
    main()