class Animal:
    def __init__(self,name,habitat,quantity):
        self.name = name
        self.habitat = habitat
        self.quantity = quantity
    
    def __str__(self):
        """ to display information about a specific animal """
        return (f"Name: {self.name}\nHabitat: {self.habitat}\nQuantity: {self.quantity}")
    
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
    
    def remove_animal(self):
        
    

