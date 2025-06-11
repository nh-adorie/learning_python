from book_store import Book, BookStore, Orders, Customer
from raw_data import books_data
import random

# Lấy dữ liệu sách từ raw data
store = BookStore()
for book in books_data:
    add_book = Book(book["id"],book["title"],book["author"],book["price"],book["quantity"])
    store.add_book(add_book)
print("\nBooks available in the store:\n")
store.display_book_list() 


orders = Orders()
title = input("\nWhat book are you looking for? ").lower()
quantity = input(f"\nHow many {title} would you like to buy")
orders.add_orders(title,quantity)


customer_name = input("\nWhat is your name? ")
customer_email = input("\nWhat is your email address? ")
customer = Customer(customer_name,customer_email,orders)





