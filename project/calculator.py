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
    return operations[opt](num1,num2)

# Header
print("Welcome to the calculator! ")

button_new = True
while button_new == True:

    # Ask for num1
    while True:
        try:
            num1 = float(input("\nWhat is the first number? "))
            break
        except Exception as e:
            print(e)
        continue

    # Ask for operator
    print("""
    + for plus
    - for substract
    * for multiply
    / for divide      
    """)

    button_continue = True
    while button_continue == True: 
        while True:
            opt = input("\nWhat is the operator? ")
            if opt in ["+","-","*","/"]:
                break
            else:
                print("Please input valid operator ")
            continue

        # Ask for num2:
        while True:
            try: 
                num2 = float(input("\nWhat is the next number? "))
                break
            except Exception as e:
                print(e)
            continue

        # The calculation
        result = calculation(num1, num2, opt)
        print(f"\n{num1} {opt} {num2} = {result}")

        # Check if user want to continue
        is_continue = input(f"\nPress 'y' to continue calculate with {result} \nPress 'n' to start a new calculation \nPress 'x' to end the program \n")
        if is_continue == "x":
            button_new = False
            button_continue = False
            print("\nGoodbye! ")
            break

        if is_continue == "n":
            button_new = True
            button_continue = False
            continue

        if is_continue == "y":
            num1 = result






    



