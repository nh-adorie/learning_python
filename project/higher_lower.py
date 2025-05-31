import game_data
import art
import random

# Constants
VALID_CHOICES = {"longer", "shorter", "same"}

def display_animal_info(animal_index, animal_indices):
    """Display information about an animal."""
    try:
        animal = game_data.animal[animal_indices[animal_index]]
        print(f"Name: \033[1m\033[32m{animal['name']}\033[0m")
        print(f"Location: {animal['location']}")
        print(f"Characteristics: {animal['characteristics']}")
    except (IndexError, KeyError) as e:
        print(f"Error accessing animal data: {e}")
        raise

def compare_lifespans(animal_index, animal_indices):
    """Compare lifespans of two animals."""
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

def get_user_choice(animal_indices, current_index, next_index):
    """Prompt user to compare lifespans and validate input."""
    prompt = f"\nDoes \033[1;32m{game_data.animal[animal_indices[current_index]]['name']}\033[0m live longer, shorter, or the same as \033[1;32m{game_data.animal[animal_indices[next_index]]['name']}\033[0m? "
    while True:
        choice = input(prompt).lower()
        if choice in VALID_CHOICES:
            return choice
        print("Please enter 'longer', 'shorter', or 'same'.")

def play_game():
    """Run the animal lifespan comparison game."""

    # Create random list of animal indices
    try:
        animal_indices = random.sample(range(len(game_data.animal)), len(game_data.animal))
    except ValueError as e:
        print(f"Error generating animal list: {e}")
        return

    score = 0
    current_index = 0
    max_index = len(animal_indices) - 1

    while current_index < max_index:
        print(f"\nAnimal No.{current_index}")
        display_animal_info(current_index, animal_indices)

        print(f"\nAnimal No.{current_index + 1}")
        display_animal_info(current_index + 1, animal_indices)

        current_animal = game_data.animal[animal_indices[current_index]]
        next_animal = game_data.animal[animal_indices[current_index + 1]]

        user_choice = get_user_choice(animal_indices,current_index, current_index + 1)
        correct_answer = compare_lifespans(current_index, animal_indices)

        print(
            f"\n{current_animal['name']} generally lives for {current_animal['longevity']} years, " 
            f"while {next_animal['name']} generally lives for {next_animal['longevity']} years")
        
        if user_choice == correct_answer:
            score += 1
            print("You got it!")            
            print(f"Your score: {score}\n")
            current_index += 1
        else:
            print(f"Wrong answer! Game over. Final score: {score}")
            break
    else:
        print(f"Congratulations! You got all answers correct. Final score: {score}")

def main():
    """Main function to start and manage the game."""
    print(art.animal_lifespan_game)
    print("Welcome to the Animal Lifespan Game!")
    print("Guess which animal has the longer lifespan!\n")

    while True:
        play_game()
        try:
            play_again = input("\nPlay again? Press 'y' to continue or any other key to quit: ").lower()
            if play_again != 'y':
                print(art.goodbye)
                break
            print("\n" * 5)
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()