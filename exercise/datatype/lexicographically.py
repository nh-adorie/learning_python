# lexicographically // theo từ điển

def lexi(word):
    # new_word = word.sort()
    # return new_word
    # Làm thế này không được vì 'str' object has no attribute 'sort'

    # Chuyển string thành list
    chars = list(word)

    # Sắp xếp list theo thứ tự alphabet. List thì có thể dùng method sort được
    chars.sort()

    # Nối lại thành từ, bằng rỗng
    new_word = ''.join(chars)
    return new_word


word = input('Please input your word, I will sort it lexicographically: ')
print('Word after sorted lexicographically is: ',lexi(word))

