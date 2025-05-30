# Blackjack // Play rules
# If the cards add up > 21 --> Bust - Lose
# If 2 cards add up < 17 --> Must take the 3rd card
# J, Q, K = 10
# A = 1 or 11 (you choose)



# Chia 1 lá bài, print cả bài của mình và của máy tính
# Chia 2 lá bài, print của mình --> Nếu là A hỏi xem lấy 1 hay 11
    # Nếu của mình < 17, chia lá thứ 3, print
    # Nếu của mình > 17, hỏi có chia nữa không
        # Nếu chia nữa --> chia lá thứ 3, print --> Nếu là A hỏi xem lấy 1 hay 11
        # Nếu dừng lại --> dừng
    # Nếu của máy tính < 17, chia lá thứ 3
    # Nếu của máy tính > 17 --> random xem có chia tiếp không
# --> Tính tổng --> Thông báo kết quả 
    # Nếu có ai > 21 --> người đó thua
    # Nếu hơn điểm --> thắng
    # ...
# import necessary libraries
import random
import art

handed_cards = []
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Create function to deal card
def deal_card():
    card = int(random.choice(cards))
    handed_cards.append(card)
    return card

# Create function to sum handed cards
def sum_cards():
    for card in handed_cards:

# Create function to handle A card
def handle_A_card(card):
    choice = int(input("What value do you want your A card to hold, 1 or 11? "))
    while True:
        if choice == 1 or choice == 11:
            card == choice
            break
        else:
            print("Please choose 1 or 11 ")
    return card




    
    
