from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date



#  CREATE MEMBER
def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


#  GET ALL MEMBERS
def get_members(db: Session):
    return db.query(models.Member).all()

# update member
def update_member(db: Session, member_id: int, member: schemas.MemberUpdate):

    db_member = db.query(models.Member).filter(models.Member.member_id == member_id).first()

    if not db_member:
        return {"error": "Member not found"} # verification of member presence in database

    db_member.name = member.name
    db_member.email = member.email
    db_member.phone = member.phone
    db_member.address = member.address

    db.commit()
    db.refresh(db_member)

    return db_member
# to delete the memeber

def delete_member(db: Session, member_id: int):

    db_member = db.query(models.Member).filter(models.Member.member_id == member_id).first()

    if not db_member:
        return {"error": "Member not found"} # checking first whether member is present in the datbase or not

    db.delete(db_member)
    db.commit()

    return {"message": "Member deleted successfully"}



#  GET ALL BOOKS
def get_books(db: Session):
    return db.query(models.Book).all()


#  GET SINGLE BOOK
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()


#  BORROW BOOK
def borrow_book(db: Session, issue: schemas.IssueCreate):

    # check book exists
    book = db.query(models.Book).filter(models.Book.book_id == issue.book_id).first()
    if not book:
        return {"error": "Book not found"}

    # check availability
    if book.copies_available <= 0:
        return {"error": "No copies available"}

    # reduce copies
    book.copies_available -= 1
    


    # create issue record
    db_issue = models.Issue(**issue.model_dump())
    db.add(db_issue)

    db.commit()
    db.refresh(db_issue)

    return db_issue


# RETURN BOOK
def return_book(db, issue_id):

    issue = db.query(models.Issue).filter(models.Issue.issue_id == issue_id).first()

    if not issue:
        return {"error": "Issue not found"}

    if issue.return_date:
        return {"error": "Book already returned"}

    issue.return_date = date.today()

    book = db.query(models.Book).filter(models.Book.book_id == issue.book_id).first()

    if book:  # IMPORTANT FIX
        book.copies_available += 1

    db.commit()

    return {"message": "Book returned successfully"}


def create_book(db: Session, book: schemas.BookCreate):

    db_book = models.Book(**book.model_dump())

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):

    db_book = db.query(models.Book).filter(models.Book.book_id == book_id).first()

    if not db_book:
        return {"error": "Book not found"}

    db_book.title = book.title
    db_book.author = book.author
    db_book.publisher = book.publisher
    db_book.publication_year = book.publication_year
    db_book.category = book.category
    db_book.copies_available = book.copies_available

    db.commit()
    db.refresh(db_book)

    return db_book



def delete_book(db, book_id):
    book = db.query(models.Book).filter(models.Book.book_id == book_id).first()

    if not book:
        return {"error": "Book not found"}  #checking, first whether the book is present or not

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}




#  GET ALL ISSUES
def get_issues(db: Session):
    return db.query(models.Issue).all()