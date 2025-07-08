# List Comprehension

# using loop
numbers = [1, 2, 3]
new_numbers = []
for number in numbers:
    new_number = number + 1
    new_numbers.append(new_number)

# using list comprehension // new_list = [new_item for item in list]
new_nums = [num + 1 for num in numbers]

# bring out the same result!

print(f"Using loop: {new_numbers} ")
print(f"Using list comprehension: {new_nums}")


double_numbers = [num*2 for num in range(1,5)]
print(f"Double numbers: {double_numbers}")

# conditional list comprehension // new_list = [new_item for item in list if test]
names = ["adorie", "foxie", "kitty", "cinamonroll", "ahri", "baymax"]

short_names = [name for name in names if len(name) < 5]
names_started_with_a = [name for name in names if name[0] == "a"]
upper_names = [name.upper() for name in names if name[-1] == "e"]

print(f"Short names: {short_names}")
print(f"Names started with letter A: {names_started_with_a}")
print(f"Uppercase names ended with letter E: {upper_names}")


# dictionary comprehension

# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key: value) in dict.items()}
# new_dict = {new_key: new_value for (key: value) in dict.items() for test}

import random
student_scores = {student: random.randint(1,100) for student in names}
print(f"Student score: {student_scores}")

passed_students = {student: student_scores[student] for student in student_scores if student_scores[student] > 60}
print(f"Passed Students: {passed_students}")

# Viết cách này thì ngắn gọn hơn
failed_students = {student: score for (student, score) in student_scores.items() if score < 60}
print(f"Failed Students: {failed_students}")



# How to iterate over a Pandas Dataframe
print("\n"*10)
student_dict = {
    "student": ["adorie", "foxie", "kitty"],
    "score": [27, 99, 58]
    }

# looping through dict
for (key, value) in student_dict.items():
    print(key)


import pandas
student_df = pandas.DataFrame(student_dict)

# looping throught dataframe
for (key, value) in student_df.items():
    print(value)

# looping throught each ROW in dataframe
for (index, row) in student_df.iterrows():
    # print(row) # dtype: object
    # print(row.score)
    if row.score > 50:
        print(row.student)

