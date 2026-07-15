from sqlalchemy import Column, Integer, String, Date,ForeignKey
from app.db import Base  # through this we can access base class and create tables in database
from datetime import date
# models for database tables

class Member(Base):
    __tablename__ = "members"

    member_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(String(255), nullable=False)
    membership_date = Column(Date, default=date.today, nullable=False)


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(100), nullable=False)
    publisher = Column(String(100), nullable=False)
    publication_year = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    copies_available = Column(Integer, nullable=False, default=0)


class Librarian(Base):
    __tablename__ = "librarians"

    librarian_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Issue(Base):
    __tablename__ = "issues"

    issue_id = Column(Integer, primary_key=True)

    member_id = Column(Integer, ForeignKey("members.member_id"))
    book_id = Column(Integer, ForeignKey("books.book_id"))
    librarian_id = Column(Integer, ForeignKey("librarians.librarian_id"))

    issue_date = Column(Date, default=date.today)
    due_date = Column(Date)
    return_date = Column(Date, nullable=True) 

