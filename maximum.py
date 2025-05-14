# Write a Python function to find the maximum of three numbers.

x = int(input('First number is'))
y = int(input('Second number is'))
z = int(input('Third number is'))

def max_of_two(x, y):
    if x > y:
        return x
    return y

# def ten_ham(tham_so):
#     # phần thân hàm
#     (return gia_tri_tra_ve) có thể có hoặc không có return

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(x, y, z)) 
