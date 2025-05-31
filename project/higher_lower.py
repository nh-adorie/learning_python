# import necessary libraries
import game_data
import random

# Choose random animal to compete
num = random.randint(0,50)
name = game_data.animal[num]["name"]
print(name)