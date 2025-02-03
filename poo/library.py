class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no está disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no ha sido prestado por {self.name}")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_books(self):
        for book in self.books:
            print(
                f"{book.title} - {book.author} - {'Disponible' if book.available else 'No disponible'}"
            )

    def show_users(self):
        for user in self.users:
            print(f"{user.name} - {user.user_id}")

book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("El túnel", "Ernesto Sábato")
book3 = Book("Cien años de soledad", "Gabriel García Márquez")
book4 = Book("El amor en los tiempos del cólera", "Gabriel García Márquez")

user1 = User("Juan", 1)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.register_user(user1)

library.show_books()

user1.borrow_book(book1)
user1.borrow_book(book2)

library.show_books()

user1.return_book(book1)

library.show_books()

user1.borrow_book(book2)

library.show_books()

user1.borrow_book(book3)

library.show_books()