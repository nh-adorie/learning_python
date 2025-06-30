class Ingredient:
    # Đại diện cho từng loại nguyên liệu: milk, water, coffee_beans, sugar, cream
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

class RecipeIngredient:
    # Đại diện cho loại nguyên liệu và định lượng trong công thức
    def __init__(self, ingredient, amount):  # ingredient là đối tượng từ class Ingredient
        self.ingredient = ingredient
        self.amount = amount

class Coffee:
    # Đại diện cho từng loại cà phê
    def __init__(self, name, recipe, price):
        self.name = name
        self.recipe = recipe  # recipe là list chứa nhiều RecipeIngredient
        self.price = price
    
    def show_recipe(self):
        # Hiển thị công thức của món cà phê
        print(f"{self.name.capitalize()} recipe: ")
        for ri in self.recipe:
            print(f"-  {ri.ingredient.name.capitalize()}: {ri.amount}{ri.ingredient.unit}")

class Stock:
    def __init__(self):
        self.stock = {}  

    def add_ingredient(self, ingredient, amount):
        # Thêm nguyên liệu vào kho
        if ingredient in self.stock:
            self.stock[ingredient] += amount
        else:
            self.stock[ingredient] = amount

    def check_stock(self, recipe):  # recipe là list chứa nhiều RecipeIngredient
        # Kiểm tra xem kho có đủ nguyên liệu cho công thức không
        for ri in recipe:
            ingredient = ri.ingredient
            required_amount = ri.amount
            if ingredient not in self.stock or self.stock[ingredient] < required_amount:
                print(f"{ingredient.name.capitalize()} out of stock")
                return False
        # Nếu đủ nguyên liệu, trừ đi
        for ri in recipe:
            self.stock[ri.ingredient] -= ri.amount
        return True

    def show_stock_status(self):
        print("Stock Status: ")
        for ingredient, amount in self.stock.items():
            print(f"-  {ingredient.name.capitalize()}: {amount}{ingredient.unit}")

class CoffeeShop:
    def __init__(self):
        self.menu = []
        self.stock = Stock()  # Tích hợp Stock vào CoffeeShop
    
    def add_coffee(self, coffee):
        self.menu.append(coffee)  # coffee là đối tượng từ class Coffee

    def show_menu(self):
        print("Menu:")
        for coffee in self.menu:
            print(f"-  {coffee.name.capitalize()}: ${coffee.price}")

    def make_coffee(self, coffee_name):
        # Tìm cà phê trong menu
        for coffee in self.menu:
            if coffee.name.lower() == coffee_name.lower():
                # Kiểm tra kho
                if self.stock.check_stock(coffee.recipe):
                    print(f"Here is your {coffee.name.capitalize()}!")
                    return
                else:
                    print(f"Sorry there is not enough ingredients to make {coffee.name.capitalize()}")
                    return
        print(f"Sorry we do not serve {coffee_name.capitalize()} yet ")

# Tạo các đối tượng Ingredient
water = Ingredient("water", "ml")
milk = Ingredient("milk", "ml")
coffee_beans = Ingredient("coffee beans", "g")
coconut = Ingredient("coconut", "ml")

# Tạo công thức
latte_recipe = [
    RecipeIngredient(water, 50),
    RecipeIngredient(milk, 40),
    RecipeIngredient(coffee_beans, 10)    
]

# Tạo đối tượng Coffee
latte = Coffee("latte", latte_recipe, 25)

# Tạo CoffeeShop và thêm latte vào menu
menu = CoffeeShop()
menu.add_coffee(latte)

# Thêm nguyên liệu vào kho
menu.stock.add_ingredient(water, 5000)
menu.stock.add_ingredient(milk, 5000)
menu.stock.add_ingredient(coffee_beans, 5000)
menu.stock.add_ingredient(coconut, 400)

# Hiển thị menu, công thức, và tình trạng kho
menu.show_menu()
latte.show_recipe()
menu.stock.show_stock_status()

# Thử pha cà phê
menu.make_coffee("latte")
menu.stock.show_stock_status()
