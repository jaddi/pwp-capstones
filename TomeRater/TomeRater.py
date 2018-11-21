class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        old_email = self.email
        self.email = address
        print("Your email has changed. Old email: {old} New email {new}".format(old = old_email, new = self.email))

    def __repr__(self):
        print("User: {user}, email: {email}, books read: {num_books}".format(user = self.name, email = self.email, num_books = len(self.books)))
    
    def __eq__(self, other_user):
        return (self.name == other_user.name and self.email == other_user.email)

    def read_book(self, book, rating = None):
        if rating >= 0 and rating <= 4:
            self.books[book] = rating
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        sum_rating = 0
        if len(self.books)>0:
            for value in self.books.values():
                sum_rating += value
            return (sum_rating / len(self.books))
        else:
            return 0

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.old_isbn = self.isbn
        self.isbn = new_isbn

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return (self.title == other_book.title and self.isbn == other_book.isbn)

    def get_average_rating(self):
        sum_rating = 0
        for value in self.ratings:
            sum_rating += value
        if len(self.ratings) > 0:
            avg_rating = (sum_rating / len(self.ratings))
        else:
            avg_rating = 0
        return avg_rating

    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __repr__(self):
        return "{title}".format(title = self.title.title())


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title.title(), author = self.author.title())

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.level = level
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title.title(), level = self.level.lower(), subject = self.subject).title()

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        self.books[new_book] = 0
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction_book = Fiction(title, author, isbn)
        self.books[new_fiction_book] = 0
        return new_fiction_book

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        self.books[new_non_fiction] = 0
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(email, rating) 
            book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email = email))
        if book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1
    
    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[new_user.email] = new_user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email, book.get_average_rating())
        
    def print_catalog(self):
        for key in self.books:
            print(key.title)

    def print_users(self):
        for user in self.users:
            print(user)
    
    def get_most_read_book(self):
        num_read_book = 0
        for book in self.books:
            if self.books[book] > num_read_book:
                num_read_book = self.books[book]
                most_read_book = book.title
        return most_read_book
        
    def highest_rated_book(self):
        book_rating = 0
        highest_rated_book = ''
        for book in self.books:
            if book.get_average_rating() > book_rating:
                book_rating = book.get_average_rating()
                highest_rated_book = book.title
        return highest_rated_book

    def most_positive_user(self):
        user_rating = 0
        most_positive_user = ''
        for user in self.users:
            if self.users[user].get_average_rating() > user_rating:
                user_rating = self.users[user].get_average_rating()
                most_positive_user = self.users[user].name
        return most_positive_user