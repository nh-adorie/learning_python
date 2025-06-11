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
    
class BookStore:
    def __init__(self):
        self.book_list = [] # là 1 list gồm nhiều obj Book

    def add_book(self, book):
        self.book_list.append(book) # Với book là obj từ class Book
    
    def display_book_list(self):
        for book in self.book_list:
            print(f"{book.title}: {book.quantity}")

    def find_book_by_title(self, title):
        for book in self.book_list:
            if book.title.lower() == title.lower():
                return book
        return None

class Orders:
    def __init__(self):
        self.ordered_books = [] # list gồm nhiều dict {book: obj Book, quantity: user input int}
        self.bill = 0 # tổng giá trị đơn hàng
        self.customer = Customer
    
    def add_orders(self, book, quantity): # book phải là obj Book
        if book.is_enough(quantity): 
            # True: còn đủ sách
            self.ordered_books.append({"book": book, "quantity": quantity, "price": book.price})
        else:
            print("Not enough books ")
    
    def summary_orders(self):
        for item in self.ordered_books: # item là 1 dict {book: obj Book, quantity: user input int}
            print(f"-  {item['book'].title}: {item['quantity']}")
            self.bill += item['book'].price # item tại ["book"] là obj Book
        print(f"Total bill: ${round(self.bill,2)}")
        return self.bill
    
class Customer:
    def __init__(self, name, email, orders):
        self.name = name #string
        self.email = email #string
        self.orders = orders #obj từ class Orders
    
    def display_customer(self):
        print(f"Customer name: {self.name}")
        print(f"Email address: {self.email}")
        self.orders.summary_orders()
    
class Management:
    def __init__(self, book_store):
        self.book_store = book_store

    def main_menu(self):
        print("Welcome to Book Shop Management Program")
        print("""
1. Add new book
2. View inventory status
3. Summary invoice list
4. Open shop
5. Close shop
""")
        while True:
            action = input("Please choose 1-5 ")
            if action not in ["1","2","3","4","5"]:
                print("Please input valid value ")
            elif action == "1":
                id = input("ID: ")
                name = input("Name: ")
                author = input("Author: ")
                price = input("Price: ")
                quantity = int(input("Quantity: "))
                book = Book(id,name,author,price,quantity)
                self.book_store.add_book(book)

            elif action == "2":
                self.book_store.display_book_list()

            elif action == "4":
                orders = Orders()
                print("Please type book title you would like to buy // or type 'quit' to end ")
                while True:
                    title = input("\nBook Title: ").lower()
                    if title == "quit":
                        break
                    else:
                        title_obj = self.book_store.find_book_by_title(title)
                        if title_obj is None:
                            print(f"{title} not found ")
                            continue
                        quantity = int(input(f"Quantity: "))        
                        orders.add_orders(title_obj, quantity)

                customer_name = input("\nWhat is your name? ")
                customer_email = input("\nWhat is your email address? ")
                customer = Customer(customer_name,customer_email, orders)

                print("Please confirm your orders as below ")
                customer.display_customer()
            elif action == "5":
                print("Goodbye ~ ")
                break
            

        

