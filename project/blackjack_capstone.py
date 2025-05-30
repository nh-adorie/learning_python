# import necessary libraries
import random
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# Create function to deal card for user (including handling A card)
def user_deal_card():
    card = int(random.choice(cards))
    if card == 11:
        print("\nYou recceive an 'A card'!")    
        while True:
            try:
                choice = int(input("What value do you want your A card to hold, 1 or 11? "))
                if choice != 1 and choice != 11:
                    print("Please choose 1 or 11 \n")
                else:
                    card = choice
                    break 
            except ValueError:
                print("Please input number 1 or 11 only \n")
        
    return card

# Create function to deal card for computer (including random A card choice)
def computer_deal_card():
    card = int(random.choice(cards))
    if card == 11:
        card = random.choice([1,11])

# The program
print(art.blackjack)
print("Welcome to Blackjack Game! ")



# User
user_sum = 0
while user_sum < 17:
    new_card = user_deal_card()
    user_sum += new_card
    print(f"You receive a {new_card} card")
    print(f"Your cards added up to {user_sum} \n")






    
    
