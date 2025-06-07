# OOP - Object Oriented Programming
# =/= Procedural Programming

# Implementing OOP

# class waiter
# object Henry, Betty # the things we used in our code
# has attributes: table_responsibile = [4,5,6]
# does methods: def take_order(), def take_payment()

# Constructing Object

# turtle: module // Turtle, Screen: class
from turtle import Turtle, Screen

# my_turtle: object 
my_turtle = Turtle()
my_screen = Screen()

# https://docs.python.org/3/library/turtle.html
my_screen.canvheight
my_screen.exitonclick()
my_turtle.shape("turtle")
my_turtle.color("pink")

# Python Packages: https://pypi.org/
# 
import cat_fact
import cat_fact.cli

fact = cat_fact.cli.cat_client.get_random_fact("cat")
print(fact)


from prettytable import PrettyTable
# PrettyTable is a class

table = PrettyTable()
# table is a object from the class PrettyTable

table.add_column("Pokemon Name",["Pikachu","Clefairy","Diglett","Meowth","Dewgong"])
table.add_column("Type",["Electric","Fairy","Ground","Normal","Water-Ice"])

print(table.align)

table.align = "l"

print(table)









