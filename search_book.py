import os 
import json
from load_book import load_book

def search_book():
    books = load_book()
    keyword = input("Enter title,author, or ISBN to search: ").lower()
    found_books = [book for book in books if keyword in book["Tittle"].lower() or keyword in book["Author"].lower() or keyword in book["ISBN"].lower()]
    
    
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(f"Title: {book['Tittle']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: {book['Price']}, Quantity: {book['Quantity']}")
    else:
        print("No matching books found.")