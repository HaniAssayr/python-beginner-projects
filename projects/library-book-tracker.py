import json
books=[]
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)
        print('Books saved successfully.')
def load_books():
    global books

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
            print("Books loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError):
        books= []

def add_book():
    try:
       year= int(input("Enter the year: ").strip())
    except ValueError:
        print("Invalid year.")
        return
    book= {
        "title" :input("Enter book title:").strip(),
        "author":input("Enter book author:").strip(),
        "year"  : year,
        "status":'available'
    }
    books.append(book)
    save_books()
    print('Book added.')

def view_books():
    if not books:
        print('No books added yet!')
        return

    print("\n----library Books----")
    for book in books:
        print(f"Title :{book['title']}")
        print(f"Author:{book['author']}")
        print(f"Year  :{book['year']}")
        print(f"Status:{book['status']}")
        print("-" * 25)

def search_books():
    if not books:
        print('No books added.')
        return
    title= input('Enter title of the book:').strip()

    for book in books:
        if book['title'].lower()== title.lower():

            print(f"Title :{book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year  :{book['year']}")
            print(f"Status: {book['status']}")
            return
    print('book not found!')
def delete_book():
    if not books:
        print('No books available:')
        return

    title= input("Enter book title:").strip()
    for book in books:
        if book['title'].lower()== title.lower():
            books.remove(book)
            save_books()
            print("Book removed successfully!")
            return

    print("Book not found!")

def update_book():
    if not books:
        print("No books available.")
        return

    title = input("Enter book title:").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            new_title = input(f"New title: ({book['title']}):").strip()
            new_author = input(f"New author: ({book['author']}):").strip()
            new_year = input(f"New year: ({book['year']}):").strip()

            if new_title:
                book['title'] = new_title

            if new_author:
                book['author'] = new_author

            if new_year:
                try:
                 book['year'] = int(new_year)

                except ValueError:
                    print("Invalid year. Keeping the current year.")

            save_books()
            print("Book updated successfully.")
            return

    print("That book is not found in the library")


def borrow_book():
    if not books:
        print("No books available.")
        return

    title= input("Enter the book title:").strip()
    for book in books:
        if book['title'].lower()== title.lower():

            if book['status']== 'available':
                book['status'] ='borrowed'
                save_books()
                print('Book borrowed successfully.')
                return

            elif book['status']== 'borrowed':
                print('Book is already borrowed.')
                return
    print("Book not found!")

def return_book():
    if not books:
        print("No books available.")
        return

    title= input("Enter book title:").strip()
    for book in books:
        if book['title'].lower()== title.lower():
            if book['status']== 'borrowed':
                book['status']= 'available'
                save_books()
                print('Book returned successfully.')
                return
            elif book['status']== 'available':
                print('Book is already on the shelf.')
                return
    print('Book not found!')

def menu():
    while True:
        print("\n----Menu----")
        print("1.Add books.")
        print("2.View books.")
        print("3.Search books.")
        print("4.Delete books.")
        print("5.Update books.")
        print("6.Borrow book.")
        print("7.Return book.")
        print("8.Exit.")

        choice = input("Enter your choice:").strip()
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            borrow_book()
        elif choice == '7':
            return_book()
        elif choice == '8':
            print("Thank you for using this program!")
            break

        else:
            print("Invalid choice.please try again.")
load_books()
menu()



