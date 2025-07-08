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

