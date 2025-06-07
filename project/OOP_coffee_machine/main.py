import coffee_data
from menu import Recipe, CoffeeDetail

coffee_recipes = coffee_data.ingredients
coffee_prices = coffee_data.coffee_prices

master_data = []

for name in coffee_prices:
    ingredients = coffee_recipes[name]
    recipe = Recipe(
        water=ingredients["water"],
        milk=ingredients["milk"],
        sugar=ingredients["sugar"],
        coffee_beans=ingredients["coffee_beans"],
        cream=ingredients["cream"]
    )
    coffee = CoffeeDetail(name, coffee_prices[name], recipe)
    master_data.append(coffee)

for name in master_data:
    name.display_coffee_info()