import coffee_data
import os
stock = coffee_data.stock

MENU = [coffee for coffee in coffee_data.ingredients]
MASTER_RECIPE = coffee_data.ingredients
INGREDIENT = [item for item in stock]
PRICE = coffee_data.coffee_prices

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_report():
    """ Function to print report """
    print(f"""
- Total revenue: # revenue
- Drinks order by customers: # type, quantity
- Stock: # ingredient, quantity left
""")

def restock(stock):
    """ Function to restock """
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
        drink = input(prompt_type)
        if drink in MENU:
            cup = valid_number(promt_quantity)
            return drink, cup
        elif drink.lower() == "no":
            return None, None
        elif drink.lower() == "close":
            print("Close! See you tommorrow")
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
    invoice = 0
    print("\nLet me confirm your order: ")
    for drink in customer_order:
        invoice += customer_order[drink] * PRICE[drink]
        if customer_order[drink] > 1:
            print(f"{customer_order[drink]} cups of {drink}")
        else:
            print(f"{customer_order[drink]} cup of {drink}")
        print(f"Total: ${invoice}")
    return invoice

def payment(invoice):
    while True:
        receive = valid_number("Please give me your money ")
        if receive < invoice:
            print("Not enough money ")
        elif receive > invoice:
            print(f"Here is your ${receive - invoice} and your coffee. Thank you ~ ")
            clear_screen()
            break
        else:
            print("Here is your coffee. Please enjoy~")
            clear_screen()
            break

def process_customer():
    customer_order = summary_order()
    check, new_stock = check_stock(customer_order)
    if check:
        invoice = issue_invoice(customer_order)
        payment(invoice)
    else:
        print("Sorry there is not enough ingredient ")
    return new_stock


# main
print("Welcome coffee shop management")
while True:
    action = input("\nChoose 'report' to view report // 'restock' to restock // 'open' to open the shop ")
    if action == "report":
        print_report()
    elif action == "restock":
        restock()
    elif action == "open":
        clear_screen()
        print(coffee_data.art)
        process_customer()
    else:
        print("Please input valid value")







    
    







