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
        print(f"Author: {self.auhtor}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
    
    def is_enough_book(self, ordered_qty):
        if ordered_qty > self.quantity:
            return False
        else:
            self.quantity -= ordered_qty
            return True

class BookStore:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book) # Với book là obj từ class Book
   
class Customer:
    def __init__(self, id, name, email, orders):
        self.id = id #string
        self.name = name #string
        self.email = email #string
        self.orders = orders #obj 
    

class Orders:
    def __init__(self, id, customer):
        self.id = id
        self.customer = customer # obj từ class Customer
        self.books = [] # list của dict
        self.bill = 0 # tổng giá trị đơn hàng
    
    def add_orders(self, book, quantity):
        if book.is_enough():
            # True: còn đủ sách
            self.books.append({"title": book, "quantity": quantity})



        


        
        






