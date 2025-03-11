import time
import random
class Book:
    def __init__(self, name, author, year, genre):
        self.name = name;
        self.author = author;
        self.year = year;
        self.genre = genre;
        pass
    def __str__(self):
        return f'{self.name} {self.author} {self.year}'
    def __repr__(self):
        return f'{self.name} {self.author} {self.year}'
    
class Libreria:
    def __init__(self, name):
        self.name = name;
        self.books = [];
        self.byAuthor = {};
        self.byYear = {};
        pass
    def __str__(self):
        return f'Libreria {self.name}'
    
    def add_book(self,book):
        self.books.append(book)
        if book.author in self.byAuthor.keys():
            self.byAuthor[book.author].append(book)
        else:
            self.byAuthor[book.author] = [book]
        
    def print_books(self):
        for a in self.books:
            print('a')
        pass
    def search_by_author_opt(self, author):
        return self.byAuthor[author]
    
    def search_by_author(self, author):
        l = []
        for a in self.books:
            if a.author == author:
                l.append(a)
        return l
NUM = 10000000

l1 = Libreria("pinco")

for i in range(0, NUM, 1):
    if random.random() * 100 > 50:
        l1.add_book(Book(f"{i}", "a", "1", ""))
    else:
        l1.add_book(Book(f"{i}", "b", "1", ""))

start1 = time.time()
l1.search_by_author("a")
end1 = time.time()

start2 = time.time()
l1.search_by_author_opt("a")
end2 = time.time()

print(f"non ott:{end1-start1} ott:{end2-start2}")