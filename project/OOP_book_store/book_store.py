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
        self.book_list = [] # là 1 list gồm nhiều obj Book

    def add_book(self, book):
        self.book_list.append(book) # Với book là obj từ class Book
    
    def display_book_list(self):
        for book in self.book_list:
            book.display_info()
    
    def display_info_by_name(self, name): # Với name là user input
        for book in self.book_list:
            if book.title == name:
                book.display_info()
            else:
                print("Book not found ")
           
# class Customer:
#     def __init__(self, id, name, email, orders):
#         self.id = id #string
#         self.name = name #string
#         self.email = email #string
#         self.orders = orders #obj từ class Orders
    
# class Orders:
#     def __init__(self, id, customer):
#         self.id = id
#         self.customer = customer # obj từ class Customer
#         self.ordered_books = [] # list gồm nhiều dict {book: obj Book, quantity: user input int}
#         self.bill = 0 # tổng giá trị đơn hàng
    
#     def add_orders(self, book, quantity):
#         if book.is_enough(): 
#             # True: còn đủ sách
#             self.ordered_books.append({"book": book, "quantity": quantity, "price": book.price})
#         else:
#             print("Not enough books ")
    
#     def summary_orders(self):
#         for item in self.ordered_books: # item là 1 dict {book: obj Book, quantity: user input int}
#             print(f"{item["book"]}: {item["quantity"]}")
#             self.bill += item["book"].price # item tại ["book"] là obj Book
#         print(f"Total bill: ${self.bill}")
#         return self.bill



    
    





        


        
        






