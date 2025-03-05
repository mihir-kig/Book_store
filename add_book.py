import os
import json

from load_book import load_book
from save_book import save_book


def add_book():
    
    books = load_book()
    
    title = input("Enter your book name:")
    author = input("Enter Book Author:")
    isbn = input("Enter of Book ISBN No.:")
    genre = input("ENter your Book Type:")
    price = float(input("Enter Book Price:"))
    quantity = input("ENter your Book Quantity:")
    
    if not title.strip():
        print("Error:Tittle must not be Empty String:")
        return
    if not price>0:
        print("Error:give Valdid Price")
        return
    if not quantity.isdigit() or int(quantity)<0:
        print("Error: Enter Non-Negative valu ")
        return
    if any(book["ISBN"] == isbn for book in books):
        print("Error This isbn Number is Exist..")
        return
    
    print("dfdfodfhohgkodfghdgiodgigiod")
    book = {
    "Tittle"  : title,
    "Author"  : author,
    "ISBN"    : isbn,
    "Genre"   : genre,
    "Price"   : price,
    "Quantity": quantity
    }
    books.append(book)
    save_book(books)