class BookStore:
    def __init__(self):
        self.book_list = [] # là 1 list gồm nhiều obj Book
        self.invoice_list = []

    def add_book(self, book):
        self.book_list.append(book) # Với book là obj từ class Book
    
    def display_book_list(self):
        for book in self.book_list:
            print(f"-  {book.title}: {book.quantity}")

    def find_book_by_title(self, title):
        for book in self.book_list:
            if book.title.lower() == title.lower():
                return book
        return None

    def add_invoice(self, customer):  # customer là obj Customer
        self.invoice_list.append(customer)

    def summary_invoice_list(self):
        if not self.invoice_list:
            print("No invoices yet.")
        for customer in self.invoice_list:
            customer.display_customer()
            print(f"Total bill: ${round(customer.orders.bill, 2)}\n")
