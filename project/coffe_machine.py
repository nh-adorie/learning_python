import coffee_data

# print our the menu
# coffee_art = coffee_data.menu
# print(coffee_art)

# List of coffee
menu = [coffee for coffee in coffee_data.ingredients]
stock = coffee_data.stock

# Create function to check valid number
def valid_number(prompt):
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
            

# Create function to ask customer their choices
def ask_for_customer_choice(prompt_type,promt_quantity):
    while True:
        choice = input(prompt_type)
        if choice in menu:
            quantity = valid_number(promt_quantity)     
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
    more_type, more_quantity = ask_for_customer_choice("\nDo you want anything else? ", "How many cups? ")
    if more_type is None:
        break
    customer_choices[more_type] = more_quantity

print("\nLet me confirm your order: ")
for type in customer_choices:
    if customer_choices[type] == 1:
        print(f"{customer_choices[type]} cup of {type}")
    else: 
        print(f"{customer_choices[type]} cups of {type}")

# Check if there sufficiant ingredient for the drinks they choose

needed_water = 0
needed_milk = 0
needed_sugar = 0
needed_coffee_beans = 0
needed_cream = 0


master_recipe = coffee_data.ingredients
ingredient = [stock for item in stock]

for type in customer_choices:
    recipe = master_recipe[type]
    for item in ingredient:
        if item == "water":
            needed_water += recipe[item] * customer_choices[type]
        elif item == "sugar":
            needed_sugar += recipe[item] * customer_choices[type]
        elif item == "milk":
            needed_milk += recipe[item] * customer_choices[type]
        elif item == "coffee_beans":
            needed_coffee_beans += recipe[item] * customer_choices[type]
        else:
            needed_cream += recipe[item]
    
print(needed_cream, needed_coffee_beans,needed_milk,needed_sugar,needed_water)
        
        
        
    
    

