# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"


# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f'{self.name} has already borrowed the maximum number of books (3).')
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f'The book "{book.title}" is already borrowed.')
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFoundException(f'{self.name} did not borrow the book "{book.title}".')
        book.is_borrowed = False
        self.borrowed_books.remove(book)

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or 'No books borrowed'
        return f'Member: {self.name}, Borrowed books: {borrowed_titles}'


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f'Book "{title}" not found in the library.')

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise ValueError(f'Member "{name}" not found in the library.')

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)

    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"