# Write a Python program to get a single string from two given strings, 
# separated by a space 
# and swap the first two characters of each string.

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def swap_character(str1, str2):
    str1_new = str2[:2] + str1[2:]
    str2_new = str1[:2] + str2[2:]
    mix_str = str2_new + str1_new
    return mix_str

str1, str2 = input('Please input your 2 strings, seperated by comma: ').split(",")
print('Your mixed string is ',swap_character(str1, str2))