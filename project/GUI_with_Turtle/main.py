import turtle
from turtle import Turtle, Screen
from random import choice, randint
my_turtle = Turtle()
my_turtle.shape("turtle")
colors  = ["pale green","moccasin","light coral","plum","light pink","light sky blue","silver"]

# draw a square
for _ in range (0,4):
  my_turtle.forward(100)
  my_turtle.left(90)
  
# draw a dash line
for _ in range (0,16):
  my_turtle.pencolor("pink")
  my_turtle.forward(2)
  my_turtle.pencolor("white")
  my_turtle.forward(2)

for _ in range (0,16):
  my_turtle.pencolor("pink")
  my_turtle.pendown()
  my_turtle.forward(2)
  my_turtle.penup()
  my_turtle.forward(2)
  
# draw square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# with random colors
for side in range (3,11):
  color = choice(colors)
  my_turtle.color(color)
  angle = 360/side
  for _ in range (0, side):
    my_turtle.forward(30)
    my_turtle.right(angle)

# draw random walk
my_turtle.width(10)
my_turtle.speed("fast") # faster, normal, ... 
directions = [0, 90, 180, 270]
for _ in range(0,100):
  angle = choice(directions)
  color = choice(colors)
  my_turtle.color(color)
  my_turtle.forward(20)
  my_turtle.setheading(angle)

# generate random colors
# tuple: immutable
def generate_rand_color():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  rand_color = (r, g, b)
  return rand_color

# # draw a spirograph
my_turtle.speed("fastest")
for _ in range (0,50):
  color = generate_rand_color()
  my_turtle.color(color)
  my_turtle.circle(75)
  my_turtle.left(10)

screen = Screen()
screen.exitonclick()