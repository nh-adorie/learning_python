import coffee_data

# print our the menu
# coffee_art = coffee_data.menu
# print(coffee_art)

# List of coffee
menu = [coffee for coffee in coffee_data.ingredients]
stock = coffee_data.stock

# Ask customer their drink choice

def ask_for_customer_choice(prompt_type,promt_quantity):
    while True:
        choice = input(prompt_type)
        if choice in menu:
            quantity = input(promt_quantity)     
            return choice, quantity
        elif choice.lower() == "no":
            return None, None
        else:
            print("Sorry we do not serve that yet 😓 Please choose other drinks available in our menu ")
        return ask_for_customer_choice(prompt_type,promt_quantity)

customer_choices = {}

type, quantity = ask_for_customer_choice("What do you want to drink? ", "How many cups? ")

customer_choices[type] = quantity

while True:
    more_type, more_quantity = ask_for_customer_choice("Do you want anything else? ", "How many cups? ")
    if more_type is None:
        break
    customer_choices[more_type] = more_quantity


# for type in customer_choices:
#     print(f"Your order is {customer_choices(type)} cup of {customer_choices}")

# Check if there sufficiant ingredient for the drink they choose
