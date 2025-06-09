class Animal:
    def __init__(self,name,habitat,quantity):
        self.name = name
        self.habitat = habitat
        self.quantity = quantity
    
    def __str__(self):
        """ to display information about a specific animal """
        return (f"Name: {self.name.capitalize()}\nHabitat: {self.habitat.capitalize()}\nQuantity: {self.quantity}")
    
    def update_quantity(self,updated_quantity):
        """ to update animal quantity """
        self.quantity += updated_quantity

class Zoo:
    def __init__(self):
        self.animal_list = []
    
    def add_animal(self,animal):
        """ to add new animal to the list """
        self.animal_list.append(animal)
    
    def display_list(self,list):
        """ to display list of animals """
        for animal in list:
            print(animal)
    
    def remove_animal(self,index):
        self.animal_list.pop(index)

    def find_animal_by_name(self,name_input):
        for animal in self.animal_list:
            if animal.name.lower() == name_input.lower():
                return animal
        return None

raw_data = [
    {"name": "lion", "habitat": "land", "quantity": 2},
    {"name": "dolphin", "habitat": "water", "quantity": 3},
    {"name": "eagle", "habitat": "air", "quantity": 1},
    {"name": "penguin", "habitat": "land", "quantity": 5},
    {"name": "shark", "habitat": "water", "quantity": 2},
    {"name": "monkey", "habitat": "land", "quantity": 7},
    {"name": "parrot", "habitat": "air", "quantity": 4},
    {"name": "whale", "habitat": "water", "quantity": 1},
    {"name": "tiger", "habitat": "land", "quantity": 3},
    {"name": "owl", "habitat": "air", "quantity": 2}
]

zoo_obj = Zoo()
for animal_dict in raw_data:
    animal_obj = Animal(animal_dict["name"],animal_dict["habitat"],animal_dict["quantity"])
    zoo_obj.add_animal(animal_obj)

animal_name = input("What animal are you searching for? ")
if zoo_obj.find_animal_by_name(animal_name) != None:
    print(f"{animal_name.capitalize()} found! Information as below: \n{zoo_obj.find_animal_by_name(animal_name)}")
else:
    print(f"{animal_name.capitalize()} not found! D")


