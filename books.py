# Book class, name
class Books:
    def __init__(self, name: str, read: bool = False):
        self.name = name
        self.read = read

    def mark_read(self):
        self.read = True

    def mark_unread(self):
        self.read = False

# Library class contains books


class Library:
    def __init__(self):
        self.books: list[Books] = []

    def add_book(self, name: str):
        book = Books(name)
        self.books.append(book)
        print(f"Added {book.name}.")

    def read_it(self, book: Books):
        book.mark_read()

    def not_read_it(self, book: Books):
        book.mark_unread()

    def search(self, name: str):
        for n in self.books:
            if name.lower() in n.name.lower():
                print(f"{n.name} is in library. Read: {n.read}")
                return
        print(f"{name} is not in library.")

    def list_all(self):
        for n in self.books:
            print(f"- {n.name} [{'Read' if n.read else 'Unread'}]")


lib = Library()
while True:
    print("\nLibrary CLI!")
    print("0 Quit | 1 Add | 2 Mark read | 3 Mark unread | 4 List all | 5 Search | 6 Stats")
    try:
        choice = int(input("> ").strip())
    except ValueError:
        print("Please choose a number! \n")
        continue
    if choice == 0:
        break
    if choice not in (1, 2, 3, 4, 5, 6):
        print("Choose number from menu!")
        continue
    elif choice == 1:
        name = input("Please add the name of the book: ").strip()
        lib.add_book(name)
    elif choice == 2:
        name = input("Please add the name of the book: ").strip()
        for n in lib.books:
            if name.lower() in n.name.lower():
                lib.read_it(n)
                print(f"Marked {name} as read.")
                break
            else:
                continue
    elif choice == 3:
        name = input("Please add the name of the book: ").strip()
        for n in lib.books:
            if name.lower() in n.name.lower():
                lib.not_read_it(n)
                print(f"Marked {name} as unread.")
                break
            else:
                continue
    elif choice == 4:
        lib.list_all()
    elif choice == 5:
        name = input("Please add the name of the book: ").strip()
        lib.search(name)
