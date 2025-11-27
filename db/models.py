from sqlalchemy import Column, DateTime, Integer, String
from .database import Base


class DbBlog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    creator = Column(String)
    title = Column(String)
    content = Column(String)
    img_url = Column(String)
    timestamp = Column(DateTime)    