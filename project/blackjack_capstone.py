# import necessary libraries
import random
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Create function to deal card for user (including handling A card)
def user_deal_card():
    card = int(random.choice(cards))
    if card == 11:
        print("\nYou recceived an 'A card'!")    
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
    return card

# Create function to pick up 3 cards and calculate cards sum
def play(who):
    scores = []
    handed_card = []
    sum = 0

    for i in range(0,3):
        if who == "user":
            card = user_deal_card()
        else:
            card = computer_deal_card()
        handed_card.append(card)

    for card in handed_card:
        sum += card
        scores.append(sum)
    
    return(handed_card, scores)

# Print line by line across all cards
def print_cards_inline(card_values):
    card_lines = [art.poker_card[str(val)].splitlines() for val in card_values]
    num_lines = len(card_lines[0])    
    for i in range(num_lines):
        print("   ".join(card[i] for card in card_lines))

# Create function to reveal result
def result(user, computer):
    print(f"\nFinal score!")
    print(f"Your cards: {user_card} → Total: {user}")
    print_cards_inline(user_card)
    print(f"\nComputer's cards: {computer_card} → Total: {computer}")
    print_cards_inline(computer_card)

    if computer > 21:
        print("Computer's cards added up more than 21. \nYou win \n☆*: .｡. o(≧▽≦)o .｡.:*☆")
    elif user > 21:
        print("Your cards added up more than 21. \nYou lose \nψ(｀∇´)ψ")
    elif computer > user:
        print("You lose ψ(｀∇´)ψ ")
    elif computer < user:
        print("You win \n☆*: .｡. o(≧▽≦)o .｡.:*☆")
    elif computer == user:
        print("Draw! \n(❁´◡`❁)")
        
# Header
print(art.blackjack)
print("Welcome to Blackjack Game! ")

# Play the game!

is_continue = True
while is_continue == True: 

    # Deal cards for user and computer
    user_card, user_scores = play("user")
    computer_card, computer_scores = play("computer")

    # Reveal the card
    print("First card!")
    print(f"You received: {user_card[0]} \n{art.poker_card[str(user_card[0])]}")
    print(f"Computer received: {computer_card[0]} \n{art.poker_card[str(computer_card[0])]}")
    input("Press Enter to reveal next card...")

    print("Second card!")
    print(f"You received: {user_card[1]} \n{art.poker_card[str(user_card[1])]} \nComputer received: secret\n")
    input("Press Enter to reveal next card...")

    if user_scores[1] > 17:
        while True:
            pick = input("Do you want to pick up another card, press y to pick, or press n to end \n").lower()
            if pick not in ["y","n"]:
                print("Please choose y or n only \n ")
            if pick == "n":
                result(user_scores[1],computer_scores[1])
                break
            if pick == "y":
                result(user_scores[2],computer_scores[2])
                break
    elif user_scores[1] <= 17:
        print("Final card!")
        print(f"You received: {user_card[2]} \n{art.poker_card[str(user_card[2])]} \nComputer received: secret\n")
        result(user_scores[2],computer_scores[2])
    
    ask = input("\nDo you want to play again? y to play or press any key to end ").lower()
    if ask != "y":
        print("Goodbye! ")
        break
    else:
        is_continue = True
        


   
    



            






    
    
