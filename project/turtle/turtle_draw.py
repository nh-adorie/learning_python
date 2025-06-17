from turtle import Turtle, Screen

adorie = Turtle()
adorie.shape("turtle")
screen = Screen()
adorie.color("pink")

def move_left():
  adorie.setheading(180)
  adorie.forward(20)

def move_right():
  adorie.setheading(0)
  adorie.forward(20)

def move_up():
  adorie.setheading(90)
  adorie.forward(20)

def move_down():
  adorie.setheading(270)
  adorie.forward(20)


screen.listen()
screen.onkey(move_left,"left")
screen.onkey(move_right,"right")
screen.onkey(move_up,"up")
screen.onkey(move_down,"down")
screen.onkey(adorie.clear,"c")