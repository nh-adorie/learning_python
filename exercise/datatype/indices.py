# print the index of a character in a string
# Sample string: w3resource
# Current character w position at 0
# ...
# Current character e position at 9

def indices(word):
    position = {}
    # chars = word.split() (Không cần vì word là chuỗi và đã có thể tách từng kí tự)
    for i in range(len(word)):
        position[i] = word[i]
    return position

word = input('Please input your word: ')
position = indices(word)
for i in range(len(word)):
    print('Current character ',position[i],' position at ',i+1)

# Không thể gán giá trị cho kết quả của một phương thức


