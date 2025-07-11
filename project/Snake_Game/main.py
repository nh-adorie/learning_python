from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

# set up screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)

# create obj
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# play 
game_is_on = True
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.reset()
        snake.reset()
    
    # Detect collision with my own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()