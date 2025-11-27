from schemas.schemas_blog import BlogBase, blogDisplay
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from db.database import get_db
from typing import List
from db import db_blog

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/create", response_model=blogDisplay)
def create_blog(request: BlogBase, db: Session = Depends(get_db)):
    blog = db_blog.create_blog(request, db)
    return blog


@router.get("/read", response_model=List[blogDisplay])
def read_all(db: Session = Depends(get_db)):
    blog = db_blog.read_all_blog(db)
    return blog


@router.put("/update", response_model=blogDisplay)
def update_post(id: int, request: BlogBase, db: Session = Depends(get_db)):
    blog = db_blog.update_blog(id, request, db)
    return blog


@router.delete("/delete", response_model=blogDisplay)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db_blog.delete_blog(id, db)
    return blog
