from turtle import Turtle, Screen
from snake import Snake
import time

# set up screen
screen = Screen()
screen.setup(width = 500, height = 500)
screen.bgcolor("black")
screen.tracer(0)

# create snake obj
snake = Snake()

# play 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()