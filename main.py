from fastapi.staticfiles import StaticFiles
from db.database import Base, engine
from fastapi import FastAPI
from router import blog


app = FastAPI()

app.include_router(blog.router)

Base.metadata.create_all(engine)

app.mount("/files", StaticFiles(directory="files"), name="files")  # makes files statically available