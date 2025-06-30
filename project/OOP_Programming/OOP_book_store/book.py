class Book:
    def __init__(self, id, title, author, price, quantity):
        self.id = id #string
        self.title = title #string
        self.author = author #string
        self.price = price #float
        self.quantity = quantity #int

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"ID: {self.id}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
    
    def is_enough(self, quantity):
        if quantity > self.quantity:
            return False
        else:
            self.quantity -=quantity
            return True