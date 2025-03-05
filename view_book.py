import os
import json
from load_book import load_book

def view_book():
    libray = load_book()
    
    if not libray:
        print("Emty Book Store")
        return
    
    for book in libray:
        print(f"Title:{book['Tittle']},Author:{book['Author']},ISBN:{book['ISBN']},Genre:{book['Genre']},Price:{book['Price']},Quantity:{book['Quantity']}")