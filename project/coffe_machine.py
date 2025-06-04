import coffee_data

# print our the menu
# coffee_art = coffee_data.menu
# print(coffee_art)

#########
menu = [coffee for coffee in coffee_data.ingredients]
stock = coffee_data.stock
master_recipe = coffee_data.ingredients
ingredient = [item for item in stock]
customer_choices = {} 
revenue = 0

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
        
        # To restock
        elif choice.lower() == "restock":
            restock()
            return None, None
        
        # To print report
        elif choice.lower() == "report":
            print(f"""
                Available ingredient: {stock}
                Total revenue: {revenue}
                Items order by customer: {customer_choices}
                  """)

        else:
            print("Sorry we do not serve that yet 😓 Please choose other drinks available in our menu ")
        return ask_for_customer_choice(prompt_type,promt_quantity)

# Create program to substract the ingredient used from stock // and restock when enter "restock"
def stock_management(stock, used):
    for item in ingredient:
        stock[item] -= used[item]

def restock():
    stock = {
    "water": 5000,
    "milk": 5000,
    "sugar": 500, 
    "coffee_beans": 500,
    "cream": 500, 
    }
    return stock

# Create function to check if there sufficiant ingredient for the drinks they choose

def check_ingredient(customer_choices):
    needed_ingredient = {
    "water": 0,
    "milk": 0,
    "sugar": 0,
    "coffee_beans": 0,
    "cream": 0,
}

    for type in customer_choices:
        recipe = master_recipe[type] 
        for item in ingredient:
            needed_ingredient[item] += recipe[item] * customer_choices[type]   

    def is_sufficient(needed):
        stock_management(stock, needed)
        return all(stock[item] >= 0 for item in ingredient)

    # If there is enough ingredient --> Confirm and continue
    # If there is not enough ingredient --> Sorry

    price = coffee_data.coffee_prices

    if is_sufficient(needed_ingredient):
        print("\nLet me confirm your order: ")
        
        for type in customer_choices:
            revenue += customer_choices[type] * price[type]
            if customer_choices[type] == 1:
                print(f"{customer_choices[type]} cup of {type}")
            else: 
                print(f"{customer_choices[type]} cups of {type}")
        print(f"Total: ${revenue}")
    else:
        print("Sorry there is not enough ingredient now. Do you want other drink? ")

# The program


def main():    
    type, quantity = ask_for_customer_choice("What do you want to drink? ", "How many cups? ")
    customer_choices[type] = quantity
    while True:
        more_type, more_quantity = ask_for_customer_choice("\nDo you want anything else? ", "How many cups? ")
        if more_type is None:
            break
        customer_choices[more_type] = more_quantity

    check_ingredient(customer_choices)



# Run the program
if __name__ == "__main__":
    main()
    
print(stock)
    

