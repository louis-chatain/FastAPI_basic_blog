from db.database import Base, engine
from fastapi import FastAPI
from router import blog


app = FastAPI()

app.include_router(blog.router)

Base.metadata.create_all(engine)
