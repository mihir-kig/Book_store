import json
import os
from load_book import load_book
from save_book import save_book

def remove_book():
    books = load_book()
    isbn = input("Enter ISBN or Book ID to remove: ")
    
    for book in books:
        if book["ISBN"] == isbn:
            books.remove(book)
            save_book(books)
            print("Book removed successfully!")
            return
    print("Error: No book found with the given ISBN")
