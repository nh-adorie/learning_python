# Write a Python function that takes a list of words 
# and return the longest word 
# and the length of the longest one.

def longest_word(sentence):
    words = sentence.split()
    length = 0
    longest = ""
    
    for word in words:
        if len(word) > length:
            length = len(word)
            longest = word
    return length, longest

sentence = input('Please input your sentence, i will find the longest word: ')
length, longest = longest_word(sentence)
print('The longest word is ',longest,' with',length,'character(s)')



