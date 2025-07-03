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
print(f"Result using loop: {new_numbers} ")
print(f"Result using list comprehension: {new_nums}")