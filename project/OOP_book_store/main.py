from book_store import Book, BookStore, Orders, Customer, Management
from raw_data import books_data

# Lấy dữ liệu sách từ raw data
store = BookStore()
for book in books_data:
    add_book = Book(book["id"],book["title"],book["author"],book["price"],book["quantity"])
    store.add_book(add_book)
print("\nBooks available in the store:\n")
store.display_book_list()


management_app = Management(store)
management_app.main_menu()








