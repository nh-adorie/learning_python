import coffee_data
import os

global stock 
stock = coffee_data.stock

global revenue
revenue = 0

MENU = [coffee.lower() for coffee in coffee_data.ingredients]
MASTER_RECIPE = coffee_data.ingredients
INGREDIENT = [item for item in stock]
PRICE = coffee_data.coffee_prices

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_report(stock, revenue):
    """ Function to print report """
    print(f"Stock status as below: ")
    for item in stock:
        print(f"{item} has {stock[item]}ml left.")
    print(f"Total revenue: {revenue}")


def restock():
    """ Function to restock """
    global stock
    stock = coffee_data.stock
    return stock

# TODO2: choose drink --> check stock --> issue invoice --> payment --> serve --> update stock

def valid_number(prompt):
    """ Function to check if user input is valid """
    while True:
        try:
            while True:
                number = int(input(prompt))
                if number <= 0:
                    print("Input shoule be a positive interger. Please try again ")
                else:
                    return number
        except ValueError:
            print("Please input valid number ")

def choose_drink(prompt_type,promt_quantity):
    """ Function to let user choose drink """
    while True:
        drink = input(prompt_type).lower()
        if drink in MENU:
            cup = valid_number(promt_quantity)
            return drink, cup
        elif drink.lower() == "no":
            return None, None
        else:
            print("Sorry we do not serve that yet. Please choose other drinks available in our menu ")
        return choose_drink(prompt_type,promt_quantity)

def summary_order():
    """ Function to summary order that customer input """
    customer_order = {}
    drink, cup = choose_drink("\nHi, what do you want to order? ", "How many cup? ")
    customer_order[drink] = cup

    while True:
        drink, cup = choose_drink("\nAnything else? ", "How many cup? ")
        if drink == None:
            break
        customer_order[drink] = cup
    
    return customer_order

def check_stock(customer_order):
    global stock
    current_stock = stock
    usage = {
        "water": 0,
        "milk": 0,
        "sugar": 0,
        "coffee_beans":0,
        "cream": 0,
    }
    for drink in customer_order: #latte
        recipe = MASTER_RECIPE[drink]
        for item in INGREDIENT: # item: water, sugar, ...
            usage[item] += recipe[item] * customer_order[drink]
    
    new_stock = {}
    for item in INGREDIENT:
        new_stock[item] = (current_stock[item] - usage[item])
    check = all(new_stock[item] > 0 for item in INGREDIENT) # True if there enough ingredient // False if not
    return check, new_stock

def issue_invoice(customer_order):
    global revenue
    invoice = 0
    print("\nLet me confirm your order: ")
    for drink in customer_order:
        invoice += customer_order[drink] * PRICE[drink]
        if customer_order[drink] > 1:
            print(f"{customer_order[drink]} cups of {drink}")
        else:
            print(f"{customer_order[drink]} cup of {drink}")
        print(f"Total: ${invoice}")
        revenue += invoice
    return invoice

def payment(invoice):
    while True:
        receive = valid_number("Please give me your money ")
        if receive < invoice:
            print("Not enough money ")
        elif receive > invoice:
            print(f"Here is your ${receive - invoice} and your coffee. Thank you ~ ")
            input("Please enter to continue")
            break
        else:
            print("Here is your coffee. Please enjoy~")
            input("Please enter to continue")          
            break

def process_customer():
    clear_screen()
    print(coffee_data.art)
    global stock
    customer_order = summary_order()
    check, new_stock = check_stock(customer_order)
    if check:
        invoice = issue_invoice(customer_order)
        payment(invoice)
        stock = new_stock
    else:
        print("Sorry there is not enough ingredient ")

# main
print("Welcome coffee shop management")

while True:
    clear_screen()
    action = ""
    while action != "next":
        prompt = """
Please choose what to do:
next    -- to welcome customer
report  -- to show summary of customer orders and stock status
restock -- to restock
close   -- to close the shop
"""
        action = input(prompt).strip().lower()
        
        if action == "close":
            print("Goodbye ~")
            exit()
        elif action == "report":
            print_report(stock, revenue)
        elif action == "restock":
            restock()
        elif action == "next":
            break 
        else:
            print("Please input a valid option.")

    process_customer()





