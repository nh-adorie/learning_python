class Recipe:
    def __init__(self,water,milk,sugar,coffee_beans,cream):
        self.water = water
        self.milk = milk
        self.sugar = sugar
        self.coffee_beans = coffee_beans
        self.cream = cream
    
    def recipe_dict (self):
        print(f"""
            Water: {self.water}ml
            Milk: {self.milk}ml
            Sugar: {self.sugar}ml
            Coffee beans: {self.coffee_beans}g
            Cream: {self.cream}ml""".strip())

class CoffeeDetail:
    def __init__(self,name,price,recipe: Recipe):
        self.name = name
        self.price = price
        self.recipe = recipe
    
    def display_coffee_info(self):
        print(f"\n{self.name.capitalize()}: ${self.price}")
        print(f"Recipe for {self.name.capitalize()}: ")
        self.recipe.display_recipe()

