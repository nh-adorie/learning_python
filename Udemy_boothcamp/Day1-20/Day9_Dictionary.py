# Dictionary {key:value}

fruits = {
    "apple": "red",
    "banana": "yellow",
    "peach": "pink",
    }

# retrieve data from dictionary
print(fruits["apple"])

# add new item to dictionary
fruits["orange"] = "orange"

# create empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
fruits = {}

# edit
fruits["apple"] = "red and green"

# loop through dictionary
for key in fruits:
    print(key)
    print(fruits[key])

# student_grades exercise:
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if 91 <= student_scores[student] <=100:
        grade = "Outstanding"
    elif 81 <= student_scores[student] <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= student_scores[student] <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student]=grade

print(student_grades)
    
# Nesting
# { key: [list],
#   key2: {dict} }

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
    "Vietnam": {"Hanoi": "Capital","HCM": "city"},
    }

# print Lille
print(travel_log["France"][1])

# print capital 
print(travel_log["Vietnam"]["Hanoi"])

# print my favorite
nested_list = ["A","B","C",{"T": "my favorite"}]
print(nested_list[3]["T"])