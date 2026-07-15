from extract import extract_books, extract_members
from transform import clean_books, clean_members
from load import load_books, load_members

def run_etl():

    print(" ETL STARTING...")

    #  STEP 1: LOAD MEMBERS FIRST
    members = extract_members()
    members = clean_members(members)
    load_members(members)

    #  STEP 2: LOAD BOOKS
    books = extract_books()
    books = clean_books(books)
    load_books(books)
    
    print("ETL loaded succesfully And..")
    
    print("ETL COMPLETED")

if __name__ == "__main__":
    run_etl()
    
