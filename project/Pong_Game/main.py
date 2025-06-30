from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# set up screen
screen  = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create obj
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# key bindings
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
