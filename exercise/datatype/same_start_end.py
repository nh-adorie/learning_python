# count the number of strings from a given list of strings. 
# The string length is 2 or more 
# and the first and last characters are the same.

import ast

def count_match(words):
    count = 0
    for word in words:
        if word[0] == word[-1]:
            count += 1
    return count

def valid_list(words):
    if not isinstance(words, list): 
        return False
    return all(isinstance(item, str) for item in words)
        

words_input = input('Input your list, eg: ["my", "cat"]: ')

try:
    # Chuyển từ chuỗi sang list thực
    words = ast.literal_eval(words_input)

    if valid_list(words):
        print('Number of words with same start and end is: ',count_match(words))
    else:
        print('Not a list')

except Exception as e:
    print('Error: ', e)


# The isinstance() function returns True 
# if the specified object is of the specified type, 
# otherwise False

# The all() function returns True 
# if all items in an iterable are true, 
# otherwise it returns False.

# try:
    # Code có thể gây lỗi
# except [LoạiLỗi]:
    # Code xử lý khi lỗi xảy ra

    # except Exception as e:  bắt mọi lỗi rồi in ra
