# OOP - Object Oriented Programming
# =/= Procedural Programming

# Implementing OOP

# class waiter
# object Henry, Betty # the things we used in our code
# has attributes: table_responsibile = [4,5,6]
# does methods: def take_order(), def take_payment()

# Constructing Object

# turtle: module // Turtle, Screen: class
# from turtle import Turtle, Screen

# # my_turtle: object 
# my_turtle = Turtle()
# my_screen = Screen()

# https://docs.python.org/3/library/turtle.html
# my_screen.canvheight
# my_screen.exitonclick()
# my_turtle.shape("turtle")
# my_turtle.color("pink")

# Python Packages: https://pypi.org/
# 
import cat_fact
import cat_fact.cli

import cat_fact.cli

# Sử dụng instance cat_client đã có sẵn từ module cli
# và gọi phương thức để lấy fact (ví dụ: .get_fact(), .fact(), .get_random_fact())
# Chúng ta cần tìm tên phương thức chính xác trong CatClient
# Thử gọi dir() trên cat_fact.cli.cat_client để xem các phương thức của nó

# Bước tạm thời để tìm phương thức đúng (sẽ làm trong terminal)
fact = cat_fact.cli.cat_client.get_fact() # Rất có thể tên hàm là này
fact = cat_fact.cli.cat_client.fact()
fact = cat_fact.cli.cat_client.random_fact()










