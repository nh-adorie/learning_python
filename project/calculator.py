# Create 4 functions for 4 operators
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# Create operations dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# Use dictionary to perform the calculation
def calculation(num1, num2, opt):
    result = operations[opt](num1,num2)
    return result

# Ask input from user
while True:
    num1 = float(input("What is the first number? "))
    print("""
    + for plus
    - for substract
    * for multiply
    / for divide      
    """)
    opt = input("What is the operator? ")
    num2 = float(input("What is the next number? "))

    is_continue = input(f"""Press 'y' to continue calculate with {result}
    Press 'n' to start a new calculation
    Press 'x' to end the program """)

