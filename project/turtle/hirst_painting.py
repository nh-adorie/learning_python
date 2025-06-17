# to play this: https://trinket.io/library/trinkets

import turtle
from turtle import Turtle, Screen
from random import choice

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.speed("fast")  # cho rùa chạy nhanh hơn: fastest

palettes = ["#F7CFD8", "#F4F8D3", "#A6D6D6", "#8E7DBE", "#BF9264", "#6F826A", "#BBD8A3", "#F0F1C5"]

my_turtle.penup()
my_turtle.goto(-100, -100)  # vị trí bắt đầu // nếu không set thì là 0,0 ở giữa trang

def draw_dot_grid(rows, cols, dot_size=15, spacing=20):
    for row in range(rows):
        for col in range(cols):
            color = choice(palettes)
            my_turtle.dot(dot_size, color)
            my_turtle.forward(spacing)
        
        # Di chuyển lên hàng mới
        my_turtle.backward(spacing * cols)  # quay về đầu dòng
        my_turtle.left(90)
        my_turtle.forward(spacing)
        my_turtle.right(90)

print("Hello buddy, lets draw a hirst painting together! ")
rows = int(input("How many rows would you like your paiting to have? "))
cols = int(input("How many columns would you like your paiting to have? "))

draw_dot_grid(rows, cols)

screen = Screen()
screen.exitonclick()