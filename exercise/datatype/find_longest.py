# Write a Python function that takes a list of words 
# and return the longest word 
# and the length of the longest one.

def longest_word(word_list):
    word_len = []
    for i in word_list:
        word_len.append(len(i)) # Thêm chiều dài của từ i vào trong list word_len
        word_len.sort() # Sắp xếp list word_len theo thứ tự từ bé đến lớn
    return word_len[-1] # Trả giá trị là độ dài lớn nhất


