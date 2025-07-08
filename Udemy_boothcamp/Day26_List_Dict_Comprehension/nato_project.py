import pandas as pd

alphabet_df = pd.read_csv("/workspaces/learning_python/Udemy_boothcamp/Day26_List_Dict_Comprehension/nato_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

print("Welcome. Please enter 1 word, or type exit to end the program")

while True:
    user_input = input("Your word: ").upper()
    if user_input == "EXIT":
        print("Goodbye ~")
        break

    if not user_input.isalpha():
        print("Invalid input. Please only enter letters.")
        continue

    try:
        result = [alphabet_dict[letter] for letter in user_input]
        print("Result:", result)
    except KeyError as e:
        print(f"Invalid letter: {e}")
