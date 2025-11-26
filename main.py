from fastapi import Depends, FastAPI, File, Request, UploadFile
from schemas.schemas_blog import BlogBase, blogDisplay
from db.database import Base, get_db, engine
from sqlalchemy.orm.session import Session
from db import db_blog


app = FastAPI()


@app.post('/create', response_model=blogDisplay)
def create_blog(request: BlogBase, db: Session = Depends(get_db)):
    # img_url = f"files/{img.filename}"
    db_blog.create_blog(request, db)
    return{
        "creator": request.creator,
        "title": request.title,
        "content": request.content,
    }
# img_url = f"../static/images/{image_name}"  # only this is send to the database

@app.get("/read")
def read_all(db: Session = Depends(get_db)):
    blog = db_blog.read_all_blog(db)
    return {
        'blogs': blog,
    }


@app.put('/update')
def update_post(id: int, request: BlogBase, db: Session = Depends(get_db)):
    db_blog.update_blog(id, request, db)
    return {
        'updated_blog': db_blog.read_blog_by_id(id, db)
    }


@app.delete('/delete')
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db_blog.read_blog_by_id(id, db)
    db_blog.delete_blog(id, db)
    return{
        'to_be_deleted': blog,
    }

Base.metadata.create_all(engine)