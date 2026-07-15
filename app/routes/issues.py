from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db import get_db

router = APIRouter(prefix="/issues", tags=["Issues"])


#  Borrow Book
@router.post("/borrow", response_model=schemas.IssueResponse)
def borrow_book(issue: schemas.IssueCreate, db: Session = Depends(get_db)):
    return crud.borrow_book(db, issue)


#  Return Book
@router.post("/return/{issue_id}")
def return_book(issue_id: int, db: Session = Depends(get_db)):
    return crud.return_book(db, issue_id)


# Get all issues
@router.get("/", response_model=list[schemas.IssueResponse])
def get_issues(db: Session = Depends(get_db)):
    return crud.get_issues(db)
