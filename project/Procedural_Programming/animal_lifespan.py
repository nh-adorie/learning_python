import game_data
import art
import random
import os

# Create function to clear the screen 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display information about an animal.
def display_animal_info(animal_index, animal_indices):
    try:
        animal = game_data.animal[animal_indices[animal_index]]
        print(f"Name: \033[1m\033[32m{animal['name']}\033[0m")
        print(f"Location: {animal['location']}")
        print(f"Characteristics: {animal['characteristics']}")
    except (IndexError, KeyError) as e:
        print(f"Error accessing animal data: {e}")
        raise

#  Function to compare lifespans of two animals.
def compare_lifespans(animal_index, animal_indices):
    try:
        current = game_data.animal[animal_indices[animal_index]]['longevity']
        next_animal = game_data.animal[animal_indices[animal_index + 1]]['longevity']
        if current > next_animal:
            return "longer"
        elif current < next_animal:
            return "shorter"
        return "same"
    except (IndexError, KeyError) as e:
        print(f"Error comparing lifespans: {e}")
        raise

# Function to prompt user to compare lifespans and validate input.
def get_user_choice(animal_indices, current_index, next_index):
    prompt = f"\nDoes \033[1;32m{game_data.animal[animal_indices[current_index]]['name']}\033[0m live longer, shorter, or the same as \033[1;32m{game_data.animal[animal_indices[next_index]]['name']}\033[0m? "
    while True:
        choice = input(prompt).lower()
        if choice in ["longer","shorter","same"]:
            return choice
        print("Please enter 'longer', 'shorter', or 'same'.")

# Run the animal lifespan comparison game.
def play_game(times):

    # Create random list of animal indices
    animal_indices = random.sample(range(len(game_data.animal)), len(game_data.animal))

    # Run the game until end of animal list
    score = 0
    current_index = 0
    max_index = len(animal_indices) - 1
    zoo = []

    while current_index < max_index:
        
        print(f"\nAnimal No.{current_index}")
        display_animal_info(current_index, animal_indices)

        print(f"\nAnimal No.{current_index + 1}")
        display_animal_info(current_index + 1, animal_indices)

        current_animal = game_data.animal[animal_indices[current_index]]
        next_animal = game_data.animal[animal_indices[current_index + 1]]

        # Compare user choice and the right answer
        user_choice = get_user_choice(animal_indices,current_index, current_index + 1)
        correct_answer = compare_lifespans(current_index, animal_indices)

        # Print out the right answer
        print(
            f"\n{current_animal['name']} generally lives for {current_animal['longevity']} years, " 
            f"while {next_animal['name']} generally lives for {next_animal['longevity']} years")
        
        # If user got the right answer
        if user_choice == correct_answer:
            score += 1
            zoo.append(art.animal_icons[current_index])
            print("You got it!")            
            print(f"Your score: {score}")
            print("".join(zoo))
            current_index += 1
            input("\nPress Enter to continue! ")
            clear_screen()

        # If user got the wrong answer    
        else:
            times -= 1
            if times > 0:
                print(f"You have {times} chance{'s' if times > 1 else ''} left.")
                input("\nPress Enter to continue! ")
                clear_screen()
                current_index += 1 
            else:
                print(f"Game over. Final score: {score}")
                break
    else:
        print(f"Congratulations! You got all answers correct. Final score: {score}")
    return times

# Main function to play the game
def main():
    clear_screen()
    print(art.animal_lifespan_game)
    print("Welcome to the Animal Lifespan Game!")
    print("Guess which animal has the longer lifespan!")
    print("There are 50 animals waiting for you to explore ~ \n ")
    
    # Choose level Easy / Medium / Hard
    while True:
        level = input("Please choose Easy, Medium or Hard level! ").lower()
        if level not in ["easy", "hard","medium"]:
            print("Invalid! Please choose again \n")
        else:
            if level == "easy":
                times = 10
                break
            elif level == "medium":
                times = 7
                break
            else:
                times = 5
                break
    clear_screen()
    
    # Continue or end the game
    while True:
        play_game(times)
        play_again = input("\nPlay again? Press 'y' to continue or any other key to quit: ").lower()
        if play_again != 'y':
            clear_screen()
            print(art.goodbye)
            break
        else:
            clear_screen()
            

# Im not sure about this but they said it's a good conventions
if __name__ == "__main__":
    main()

    