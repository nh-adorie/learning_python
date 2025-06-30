HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
word_list = ["strawberry","grape","lemon","orange","mango"]
chosen_word = random.choice(word_list)

print("Let's play hangman!. Guess this word: ")

lives = 6
guessed_letter = []
display = ['_'] * len(chosen_word)

print(''.join(display))


while lives > 0 and "_" in display:
    user_guess = input('What is your guess? ')

    if user_guess in guessed_letter:
        print('You guesed this letter. Try again')
        continue

    if user_guess in chosen_word:       
        for index, char in enumerate(chosen_word):
            if user_guess == char:
                display[index] = user_guess
    else:
        lives = lives - 1
        print("You have",lives,"lives left")
        print(HANGMANPICS[6-lives])              
    print(''.join(display))

    if lives <=0:
        game_over = True

if "_" not in display:
    game_over = True
    print("You win ╰(*°▽°*)╯")
else:
    print("Die ψ(｀∇´)ψ. The word was",chosen_word)

