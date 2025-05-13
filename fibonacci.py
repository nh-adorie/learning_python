# Write a Python program to get the Fibonacci series
# The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.

num = input('How many fibonacci number do you want to write?')

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(int(num)):
    print(fibonacci(i), end=" ")


# if điều_kiện:
    # code này chạy nếu điều_kiện đúng (True)
# code dưới đây sẽ chạy nếu điều_kiện sai (False)