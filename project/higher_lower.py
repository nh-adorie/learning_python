# import necessary libraries
import game_data
import random

# Choose random animal to compete
def choose_animal():
    num = random.randint(0,49)
    print(f"\nName: {game_data.animal[num]['name']}")
    print(f"Location: {game_data.animal[num]['location']}")
    print(f"Characteristics: {game_data.animal[num]['characteristics']}")
    longevity = game_data.animal[num]['longevity']
    name = game_data.animal[num]['name']
    return longevity, name

# Compare longevity of 2 animal to get the answer
def compare(longevity1,longevity2):
    ans = ""
    if longevity2 < longevity1:
        return "shorter"
    elif longevity2 > longevity1:
        return "longer"
    else:
        return "same"

# Pick 2 animal to start the comparing game
longevity1, name1 = choose_animal()
longevity2, name2 = choose_animal()
print(f"\nComparing {name2}'s longevity and {name1}'s longevity, what do you think? ")

# Let user choose which one live longer
while True:
    user_choice = input(f"Please choose 'longer', 'shorter', or 'same' ").lower()
    if user_choice not in ["longer","shorter","same"]:
        print("Please input valid choice! ")
    else:
        break

# Compare user choice and the right answer
answer = compare(longevity1,longevity2)
if answer == user_choice:
    print("You got it! Next! ")
else:
    print("Wrong answer! Game over! ")
    print(f"{name1} lives for {longevity1} years.")
    print(f"{name2} lives for {longevity2} years.")
    print(f"{name2} lives {answer} to {name1}")

# 
# print(answer)
    



    
