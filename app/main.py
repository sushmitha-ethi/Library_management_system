

from fastapi import FastAPI
from app.routes import members, books, issues
app = FastAPI()
app.include_router(members.router)
app.include_router(books.router)
app.include_router(issues.router)


@app.get("/")
def read_root():
    return {"message": "Library Management API is running"}



'''@app.get("/")
def root():
    return {
        "message": "Library Management System API",
        "endpoints": {
            "members": "/members",
            "books": "/books",
            "issues": "/issues"
        },
        "docs": "/docs"
    }'''

'''from fastapi.responses import FileResponse

@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")'''