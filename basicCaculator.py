num1, op, num2 = input('What do you want to calculate? (e.g., 7 + 2): ').split()

num1 = int(num1)
num2 = int(num2)

def calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Sorry I can not do it now :( "

result = calculator(num1, op, num2)

print("Result is:", result)


