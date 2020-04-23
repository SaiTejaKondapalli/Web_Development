import os, csv
from Database import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
db = db_session()

b = open("books.csv")
books = csv.reader(b)
i = 0
for ISBN, title, author, year in books:
    if i != 0:
        book = Book(isbn=ISBN, title=title, author=author, year=year)
        print(book.title)
        db.add(book)
    i += 1
db.commit()
db.close()