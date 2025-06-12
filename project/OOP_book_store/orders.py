class Orders:
    def __init__(self):
        self.ordered_books = [] # list gồm nhiều dict {book: obj Book, quantity: user input int}
        self.bill = 0 # int tổng giá trị đơn hàng
    
    def add_orders(self, book, quantity): # book phải là obj Book
        if book.is_enough(quantity): 
            # True: còn đủ sách
            self.ordered_books.append({"book": book, "quantity": quantity, "price": book.price})
        else:
            print("Not enough books ")
    
    def calculate_total(self):
        self.bill = sum(item['book'].price * item['quantity'] for item in self.ordered_books)
        return self.bill
    
    def summary_orders(self):
        for item in self.ordered_books: # item là 1 dict {book: obj Book, quantity: user input int}
            print(f"-  {item['book'].title}: {item['quantity']}")
            self.bill += item['book'].price # item tại ["book"] là obj Book
        print(f"Total bill: ${round(self.bill,2)}")
        return self.bill