import os
import csv
import pandas

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path,"weather_data.csv")

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
