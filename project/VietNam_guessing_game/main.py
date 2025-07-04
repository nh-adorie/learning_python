import turtle
import os
import pandas

current_path = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.title("Vietnam Cities Game")

city_name = turtle.Turtle()
city_name.hideturtle()
city_name.penup()

# đặt ảnh nền thành bản đồ Việt Nam
image_path = os.path.join(current_path, "vietnam_map.gif")
screen.bgpic(image_path)

# có thể tự lấy tọa độ x, y dựa theo vị trí click chuột như sau:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# đọc file csv
cities_path = os.path.join(current_path, "cities.csv")
data = pandas.read_csv(cities_path)

all_cities = data.city.to_list()
guessed = []

while len(guessed) < 34:
    answer = screen.textinput(title = f"{len(guessed)}/34 cities correct", prompt = "What's another city's name? ").title()
    if answer == "Exit":

        # lưu những thành phố chưa đoán được vào 1 file
        missing_cities = []
        for city in all_cities:
            missing_cities = [city for city in all_cities if city not in guessed]
            df_missing = pandas.DataFrame(missing_cities, columns=["Missing Cities"])
            new_path = os.path.join(current_path, "missing_cities.csv")
            df_missing.to_csv(new_path, index=False)
        break  
    answer = answer.strip().title()
    
    for city in all_cities:
        if city == answer and city not in guessed:

            # hiện tên những thành phố đoán đúng
            guessed.append(city)
            city_data = data[data.city == city]
            x = city_data.x.values[0]
            y = city_data.y.values[0]
            city_name.goto(x, y)
            city_name.write(answer, align="center", font=("Arial", 8, "normal"))
            break

turtle.mainloop()
