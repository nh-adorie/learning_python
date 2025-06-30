print("Welcome to the blind auction!")

# ask input from user, break when there is none who want to bid
# pass those input into a dictionary

dict = {}

while True:
    name = input("\nWhat is your name? ")

    while True:
        try:
            bid = float(input("\nHow much do you want to bid? $"))
            break
        except Exception as e:
            print(e)
            print("Please input number only")

    dict[name] = bid
    choice = input("\nIs there other person who want to bid? \nType yes to continue \nPress any other key to end and see result!\n").lower()
    if choice != "yes":
        break
    else:
        print("\n"*100)
        
# compare bid from the dictionary

def find_winner(dict):
    biggest_bid = 0
    winner = ""
    for person in dict:
        if dict[person] > biggest_bid:
            biggest_bid = dict[person]
            winner = person
    return winner, biggest_bid

print("\n"*100)
winner, biggest_bid = find_winner(dict)
print(f"The winner is {winner} with the bid of {biggest_bid}$")




