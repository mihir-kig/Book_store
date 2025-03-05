from add_book import add_book
from remove_book import remove_book
from view_book import view_book
from search_book import search_book

def main():
    while True:
        print("\n Book Store Management System")
        print("1.Add Book")
        print("2.View Book")
        print("3.Search Book")
        print("4.Remove Book")
        print("5.Exit")
        choice = int(input("Enter Your Choice(1-5):"))
        
        if choice == 1:
            add_book()
        elif choice==2:
            view_book()
        elif choice == 3:
            search_book()
        elif choice==4:
            remove_book()    
        elif choice==5:
            print("Exit...")
            break
        else:
            print("Please Enter the valid Choice")
            
if __name__ == "__main__":
    main()
   