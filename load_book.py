
import os
import json
def load_book():
    BOOKS_FILE = "book_list.json"
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE,"r") as file:
            return json.load(file)
    return []
    