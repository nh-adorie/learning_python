# Given an array arr. 
# Your task is to find the minimum and maximum elements in the array.

def min_max(numbers):
    min = numbers[0]
    max = number[0]
    for number in numbers:
        if number >= min:
            min = number
        