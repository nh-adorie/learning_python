# Factorial // Giai thừa
# 4! = 4 * 3 * 2 * 1 =24

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

try:
    input_num = input('Enter a non-negative integer to calculate factorial:')
    num = int(input_num)

    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    elif num > 100:
        print('Too large number, can not calculate :(')
    else:
        print('Factorial of ',num,'is ',factorial(num))

except ValueError:
    print("Error: Please enter a valid integer.")


