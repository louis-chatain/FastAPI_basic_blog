import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.schemas_blog import BlogBase
from db.models import DbBlog


def create_blog(request: BlogBase, db: Session):
    new_blog = DbBlog(
        creator=request.creator,
        title=request.title,
        content=request.content,
        img_url=request.img_url,
        timestamp=datetime.datetime.now(),
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
    return blog


def delete_blog(id: int, db: Session):
    blog = db.query(DbBlog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog id {id} not found."
        )
    db.delete(blog)
    db.commit()
    return blog
