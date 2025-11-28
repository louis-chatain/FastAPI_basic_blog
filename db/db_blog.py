from fastapi import File, HTTPException, UploadFile, status
from sqlalchemy.orm.session import Session
from schemas.schemas_blog import BlogBase
from db.models import DbBlog
from datetime import datetime
import shutil
import os

def create_blog(
    creator: str,
    title: str,
    content: str,
    db: Session,
    img_request: UploadFile = File(Ellipsis),
):
    file_location = f"files/{img_request.filename}"
    with open(file_location, "w+b") as buffer:
        shutil.copyfileobj(img_request.file, buffer)

    new_blog = DbBlog(
        creator=creator,
        title=title,
        content=content,
        img_url=file_location,
        timestamp=datetime.now().date(),
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def read_all_blog(db: Session):
    blog = db.query(DbBlog).all()
    return blog


def read_blog_by_id(id: int, db: Session):
    blog = db.query(DbBlog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog id {id} not found."
        )
    return blog


def update_blog(id: int, request: BlogBase, db: Session):
    blog = db.query(DbBlog).filter_by(id=id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog id {id} not found."
        )
    blog.update(
        {
            DbBlog.creator: request.creator,
            DbBlog.title: request.title,
            DbBlog.content: request.content,
        }
    )
    db.commit()
    blog = db.query(DbBlog).filter_by(id=id).first()
    return blog


def delete_blog(id: int, db: Session):
    blog = db.query(DbBlog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog id {id} not found."
        )
    img_location = blog.img_url
    if os.path.exists(img_location):
        os.remove(img_location)
        print(f"File '{img_location}' deleted successfully.")
    else:
        print(f"File '{img_location}' not found.")
    db.delete(blog)
    db.commit()
    return blog
