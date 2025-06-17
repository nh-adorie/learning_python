from turtle import Turtle, Screen
from random import randint

# set up screen
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

# set up the turtles
all_turtles = []
colors = ["orange", "blue", "green", "yellow", "red", "pink"]

for index in range(6):  # index: 0 -> 5
    my_turtle = Turtle()
    my_turtle.penup()
    my_turtle.shape("turtle")
    my_turtle.color(colors[index])
    my_turtle.goto(-230, 100 - index * 40)
    all_turtles.append(my_turtle)

# dùng textinput thay vì input()
user_choice = input("Which turtle will win the race? (orange, blue, green, yellow, red, pink)")
if user_choice:
    user_choice = user_choice.strip().lower()
    is_race_on = True

while is_race_on:
    for current_turtle in all_turtles:
        if current_turtle.xcor() > 230:
            is_race_on = False
            winning_color = current_turtle.color()[0]
            print("The winner is", winning_color, "turtle!")
            if winning_color.lower() == user_choice:
                print("You win!")
            else:
                print("You lose.")
            break
        current_turtle.forward(randint(1, 10))

screen.exitonclick()
