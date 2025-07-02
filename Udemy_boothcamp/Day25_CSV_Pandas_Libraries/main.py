import os
import csv
import pandas

current_path = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_path,"weather_data.csv")

# with open(file_path, mode = "a") as weather_file:
#     weather_file.write("\nTuesday,18,Rainy")

# with open(file_path) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             # print(type(row)) // row is a list
#             temp = row[1]
#             temperatures.append(int(temp))

# print(temperatures)

# data = pandas.read_csv(file_path)
# print(type(data)) # pandas.core.frame.DataFrame (dataframe ~ table) 
# print(type(data["temp"])) # pandas.core.series.Series (series ~ list ~ column)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = data["temp"].mean()
# print(average_temp)

# print(f"Maximum temperature: {data['temp'].max()}")
# print(f"Miniimum temperature: {data['temp'].min()}")
# print(f"Average temperature: {data['temp'].mean()}")

# Get data in column
# print(data["condition"])
# print(data.condition) # the same

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# tuesday = data[data.day == "Tuesday"] # tuesday is a dataframe

# Create new dataframe from scratch
# data_dict = {
#     "student" : ["adorie", "foxie", "kitty"],
#     "score" : ["2", "7", "10"]
# }

# student_data = pandas.DataFrame(data_dict)
# print(student_data)
# student_data_path = os.path.join(current_path,"student_data.csv")
# student_data.to_csv(student_data_path)

squirrel_path = os.path.join(current_path, "squirrel.csv")
raw = pandas.read_csv(squirrel_path)
count = raw["Primary Fur Color"].value_counts()
new_file = pandas.DataFrame(count)
new_file_path = os.path.join(current_path, "squirrel_count.csv")
new_file.to_csv(new_file_path)

