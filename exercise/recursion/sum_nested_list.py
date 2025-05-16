def sum_nested_list(list_data):
    total = 0
    for x in list_data:
        if isinstance(x, list):  # Kết quả của hàm này là boolean
            total = total + sum_nested_list(x)
        else:
            total = total + x
    return total

print('Sum of nested list: ',sum_nested_list([1,2,[3,4]]))