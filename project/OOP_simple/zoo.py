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

    def find_animal_by_name(self,name_input):
        for animal in self.animal_list:
            if animal.name.lower() == name_input.lower():
                return animal
        return None
    
    def find_animal_by_habitat(self,habitat_input):
        list_by_habitat = []
        for animal in self.animal_list:
            if animal.habitat.lower() == habitat_input.lower():
                list_by_habitat.append(animal)
        return list_by_habitat
    
    def find_index_of_animal(self,animal, list):
        index = list.index(animal)
        return index

    def total_animal_by_habitat(self,list):
        total = 0
        for animal in list:
            total += animal.quantity
        return total
    
    def update_quantity_by_name(self, name, new_quantity):
        animal = self.find_animal_by_name(name)
        if animal:
            animal.quantity = new_quantity
            return True
        return False

    def display_status(zoo):
        print("===== Current Zoo State =====")
        for animal in zoo.animal_list:
            print(animal)
            print("---")
        print("=============================")


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

# Find by name
print("Find animal by name: Please enter animal name to find out its information. Type 'quit' to end ")
while True:
    animal_name = input("Animal name: ")
    if animal_name == "quit":
        print("Goodbye ~ ")
        break
    elif zoo_obj.find_animal_by_name(animal_name) != None:
        print(f"{animal_name.capitalize()} found! Information as below: \n{zoo_obj.find_animal_by_name(animal_name)}")
    else:
        print(f"{animal_name.capitalize()} not found! ")

# Find by habitat:
print("Find animals by habitat: Please enter animal's habitat. Type 'quit' to end ")
while True:
    input_habitat = input("\nAnimal habitat: ")
    result = zoo_obj.find_animal_by_habitat(input_habitat)
    if input_habitat not in ["land", "water","air","quit"]:
        print("Please input valid habitat ")
    elif input_habitat == "quit":
        print("Goodbye ~")
        break
    else:
        print(f"Animals live in {input_habitat} includes: ")
        for animal in result:
            print(str(animal))
            print("---")
            print(f"Total animals live in {input_habitat}: {zoo_obj.total_animal_by_habitat(result)}")

# Add new animal:
new_animal = Animal("elephant","land",5)
zoo_obj.add_animal(new_animal)

# Update new quantity:
zoo_obj.update_quantity_by_name("tiger",7)

zoo_obj.display_status()