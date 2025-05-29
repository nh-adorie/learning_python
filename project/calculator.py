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

# Create function to use dictionary to perform the calculation
def calculation(num1, num2, opt):
    result = operations[opt](num1,num2)
    return result

# Ask input from user
while True:
    # Ask for num1
    try:
        num1 = float(input("What is the first number? "))
        break
    except Exception as e:
        print(e)
    
    # Ask for operator
    print("""
    + for plus
    - for substract
    * for multiply
    / for divide      
    """)
    while True:
        opt = input("What is the operator? ")
        if opt in ["+","-","*","/"]:
            break
        else:
            print("Please input valid operator ")

# Ask for num2:
while True:
    try: 
        num2 = float(input("What is the next number? "))
        break
    except Exception as e:
        print(e)






while True:
    is_continue = input(f"""Press 'y' to continue calculate with {result}
    Press 'n' to start a new calculation
    Press 'x' to end the program """)
    if is_continue == "y":


