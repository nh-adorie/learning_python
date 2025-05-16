# Write a Python program to count the number of characters (character frequency) in a string.
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# {}


def count_frequency(string):
    freq = {}
    for x in string:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

string = input('Please input string: ')
print('Character frequency: ',count_frequency(string))
