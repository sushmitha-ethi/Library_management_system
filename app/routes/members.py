
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db import get_db

router = APIRouter(prefix="/members", tags=["Members"])



#  Create Member
@router.post("/", response_model=schemas.MemberResponse)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db, member)


#  Get All Members
@router.get("/", response_model=list[schemas.MemberResponse])
def get_members(db: Session = Depends(get_db)):
    return crud.get_members(db)

# update memebr
@router.put("/{member_id}", response_model=schemas.MemberResponse)
def update_member(member_id: int, member: schemas.MemberUpdate, db: Session = Depends(get_db)):
    return crud.update_member(db, member_id, member)

# delete member

@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    return crud.delete_member(db, member_id)