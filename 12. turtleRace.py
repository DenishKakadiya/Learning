import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

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

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def race(colors):
    turtles = create_turtle(colors)
    print(type(turtles))

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 20:
                return colors[turtles.index(racer)]

def create_turtle(colors) -> list:
    turtles = []
    spacingx = WIDTH / (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.left(90)
        racer.shape("turtle")
        racer.penup()
        racer.setpos(spacingx*(i+1) - WIDTH/2, -200)
        racer.pendown()
        turtles.append(racer)
       
    return turtles

def main():
    racers = get_no_of_racers()
    print(racers)
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    winner = race(colors)
    print(f"Winning turtle is the turtle with color {winner}")
    time.sleep(4)


if __name__ == "__main__":
    main()