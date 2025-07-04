# Filtering Even Numbers
# In this list comprehension exercise you will practice using list comprehension 
# to filter out the even numbers from a series of numbers. 

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
print(result) 