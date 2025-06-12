from customer import Customer
from book import Book
from orders import Orders

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
                price = int(input("Price: "))
                quantity = int(input("Quantity: "))
                book = Book(id,name,author,price,quantity)
                self.book_store.add_book(book)

            elif action == "2":
                self.book_store.display_book_list()
            
            elif action == "3":
                self.book_store.summary_invoice_list()

            elif action == "4":
                orders = Orders()
                print("Please type book title you would like to buy // or type 'quit' to end ")
                while True:
                    title = input("\nBook Title: ").lower()
                    if title == "quit":
                        break
                    title_obj = self.book_store.find_book_by_title(title)
                    if not title_obj:
                        print(f"{title} not found ")
                        continue
                    quantity = int(input("Quantity: "))
                    orders.add_orders(title_obj, quantity)

                orders.calculate_total()
                
                customer_name = input("\nWhat is your name? ")
                customer_email = input("\nWhat is your email address? ")
                customer = Customer(customer_name, customer_email, orders)

                print("\n--- Order Summary ---")
                customer.display_customer()
                orders.summary_orders()

                # Lưu đơn hàng vào BookStore
                self.book_store.add_invoice(customer)

            elif action == "5":
                print("Goodbye ~ ")
                break
