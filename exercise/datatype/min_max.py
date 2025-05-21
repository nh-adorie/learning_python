# Given an array arr. 
# Your task is to find the minimum and maximum elements in the array.

def min_max(numbers):
    min = numbers[0]
    max = number[0]
    for number in numbers:
        if number <= min:
            min = number
        if number >= max:
            max = number
    return min max

numbers = input("Please input your numbers, seperated by comma").split(",")
output_min, output_max = min_max(numbers)
print("The biggest number in your list is", output_max, "and the smallest number is ",output_min)


        
        
