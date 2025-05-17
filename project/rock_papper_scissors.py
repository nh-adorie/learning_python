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