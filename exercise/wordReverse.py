# Write a Python program that accepts a word from the user and reverses it.

word = input('What word do you want to reverse baby?')

for char in range(len(word)-1,-1,-1):
    print(word[char], end="")

# (start stop step)

# Ví dụ từ Hello
# len = 5 --> char in range(4,-1,-1) --> 4, 3, 2, 1, 0, (-1)
