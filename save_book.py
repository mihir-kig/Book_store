import os
import json
def save_book(books):
    BOOK_FILE = "book_list.json"
    with open(BOOK_FILE,"w") as file:
        json.dump(books,file,indent=4)
    