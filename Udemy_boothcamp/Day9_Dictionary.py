# Dictionary {key:value}
# Nesting

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
# fruits = {}

# edit
fruits["apple"] = "red and green"

# loop through dictionary
for key in fruits:
    print(key)
    print(fruits[key])
