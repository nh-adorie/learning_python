import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

papper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

rock_papper_scissor = [rock,papper,scissor]
computer_choice = random.choice(rock_papper_scissor)
your_choice = input ("""
Rock! Papper! Scissor! ( •̀ ω •́ )y( •̀ ω •́ )
Please input Rock or Papper or Scissor
""")

if your_choice.lower() == "rock" and computer_choice == papper:
    print("Your choice: ", rock)
    print("Computer choice: ", papper)
    print("You lose") 

if your_choice.lower() == "rock" and computer_choice == rock:
    print("Your choice: ", rock)
    print("Computer choice: ", rock)
    print("Play again")

if your_choice.lower() == "rock" and computer_choice == scissor:
    print("Your choice: ", rock)
    print("Computer choice: ", scissor)
    print("You win")

if your_choice.lower() == "papper" and computer_choice == papper:
    print("Your choice: ", papper)
    print("Computer choice: ", papper)
    print("Play again") 

if your_choice.lower() == "papper" and computer_choice == rock:
    print("Your choice: ", papper)
    print("Computer choice: ", rock)
    print("You win")

if your_choice.lower() == "papper" and computer_choice == scissor:
    print("Your choice: ", papper)
    print("Computer choice: ", scissor)
    print("You lose")

if your_choice.lower() == "scissor" and computer_choice == papper:
    print("Your choice: ", scissor)
    print("Computer choice: ", papper)
    print("You win") 

if your_choice.lower() == "scissor" and computer_choice == rock:
    print("Your choice: ", scissor)
    print("Computer choice: ", rock)
    print("You lose")

if your_choice.lower() == "scissor" and computer_choice == scissor:
    print("Your choice: ", scissor)
    print("Computer choice: ", scissor)
    print("Play again")

if your_choice != "rock" and your_choice != "papper" and your_choice != "scissor":
    print("Please input valid value")


# Another way:
# Rock = 0, Paper = 1, Scissor = 2
# your = computer --> Play again
# you == 0 // computer == 2 --> you win
# you == 2 // computer == 0 --> you lose
# you > computer --> you win
# you < computer --> you lose