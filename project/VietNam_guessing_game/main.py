import turtle
import os

current_path = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.title("Vietnam Cities Game")

# đặt ảnh nền thành bản đồ Việt Nam
image_path = os.path.join(current_path, "vietnam_map.gif")
screen.screensize()
screen.bgpic(image_path)



screen.exitonclick()
