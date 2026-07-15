from pydantic import BaseModel
from datetime import date


#  1. MEMBERS SCHEMA

class MemberBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class MemberCreate(MemberBase):
    pass


class MemberResponse(MemberBase):
    member_id: int
    membership_date: date

    class Config:
        from_attributes = True

class MemberUpdate(MemberBase):
    pass


#  2. BOOKS SCHEMA

class BookBase(BaseModel):
    title: str
    author: str
    publisher: str
    publication_year: int
    category: str
    copies_available: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    book_id: int

    class Config:
        from_attributes = True
        
# BOOK CREATE (for POST)

class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    publication_year: int
    category: str
    copies_available: int


#  BOOK UPDATE (for PUT)

class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    publication_year: int
    category: str
    copies_available: int


#  3. LIBRARIANS SCHEMA

class LibrarianBase(BaseModel):
    name: str
    email: str


class LibrarianCreate(LibrarianBase):
    pass


class LibrarianResponse(LibrarianBase):
    librarian_id: int

    class Config:
        from_attributes = True


#  4. ISSUES SCHEMA

class IssueBase(BaseModel):
    member_id: int
    book_id: int
    librarian_id: int
    due_date: date


class IssueCreate(IssueBase):
    pass


class IssueResponse(IssueBase):
    issue_id: int
    issue_date: date
    return_date: date | None

    class Config:
        from_attributes = True
