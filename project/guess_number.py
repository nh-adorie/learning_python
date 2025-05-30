import art
import random 

print(art.guess_number)
print("Welcome to Guess the number Game!")

# Create a function to guess number
def guess_number(number,lives,answer):

    if number > answer:
        print("Too high! ")
        lives -=1
        print(f"You have {lives} guesses left")
        
    elif number < answer: 
        print("Too low! ")
        lives -=1
        print(f"You have {lives} guesses left")

    elif number == answer:
        print(f"Congratulation! You win!")
        lives = -1 # as win

    if lives == 0:
        print("\nRun out of guesses. You lose! ")

    return lives

# Play the game 


while True:

    # Choose game mode
    while True:
        level = input("\nPress E for Easy mode or press H for Hard mode ").upper()
        if level not in ["E","H"]:
            print("Invalid! Choose again ")
        else:
            break

    if level == "E":
        times = 10
        print(f"\nEasy Mode (❁´◡`❁): You have {times} guesses")
    else:
        times = 5
        print(f"\nHard Mode ψ(｀∇´)ψ: You have {times} guesses ")

    answer = random.randint(1,100)
    print(f"\nI'm thinking of a number between 1 and 100.")
    

    # User guess the number 
    while times > 0:
        
        while True:
            try:
                user_guess = int(input("\nMake a guess! "))
                break
            except Exception as e:
                print(e)
                print("Invalid! Please input a number ")
        
        times = guess_number(user_guess,times,answer)

    print(f"\nThe correct number is {answer}")

    choice = input("Do you want to play again? Press Y to play or any other key to end ").upper()
    if choice != "Y":
        print(art.goodbye)
        break

