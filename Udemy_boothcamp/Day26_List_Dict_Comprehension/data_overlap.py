# Data Overlap
# 💪 This exercise is HARD 💪 

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

# You are going to create a list called result which contains the numbers that are common in both files. 

with open("Udemy_boothcamp/Day26_List_Dict_Comprehension/file1.txt") as file_1:
    numbers_1 = [number.strip() for number in file_1]

with open("Udemy_boothcamp/Day26_List_Dict_Comprehension/file2.txt") as file_2:
    numbers_2 = [number.strip() for number in file_2]

result = [int(number) for number in numbers_1 if number in numbers_2]
print(result)

