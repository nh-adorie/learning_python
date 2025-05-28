print("Welcome to the blind auction!")

# ask input from user, break when there is none who want to bid
# pass those input into a dictionary

dict = {}

while True:
    name = input("\nWhat is your name? ")

    while True:
        try:
            bid = float(input("How much do you bid? "))
            break
        except Exception as e:
            print(e)
            print("Please input number only")

    dict[name] = bid
    choice = input("Is there other person who want to bid? (type yes to continue) ").lower()
    if choice != "yes":
        break
    else:
        print("\n"*100)
        
# look for the biggest bid from the dictionary

winner = ""
biggest_bid = 0

for person in dict:
    if dict[person] > biggest_bid:
        biggest_bid = dict[person]
        winner = person

print("\n"*100)
print(f"The winner is {winner} with the bid of {biggest_bid}")




