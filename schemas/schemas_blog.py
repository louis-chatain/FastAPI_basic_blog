from datetime import datetime
from fastapi import File, UploadFile
from pydantic import BaseModel

#-----------------------------------------------------------------------------
class BlogBase(BaseModel):      # data that we will demand/receive from the user
    creator: str
    title: str
    content: str
    img_url: str

class blogDisplay(BaseModel):   # data that we will send back to the user                                   
    id: int
    creator: str                # sends back only username and email in
    title: str                  # the response body in the docs
    content: str
    img_url: str
    timestamp: datetime
    class ConfigDict():
        from_attributes = True
#-----------------------------------------------------------------------------