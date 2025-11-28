from pydantic import BaseModel
from datetime import date

#-----------------------------------------------------------------------------
class BlogBase(BaseModel):      # data that we will demand/receive from the user
    creator: str
    title: str
    content: str


class blogDisplay(BaseModel):   # data that we will send back to the user                                   
    id: int
    creator: str                # sends back only username and email in
    title: str                  # the response body in the docs
    content: str
    img_url: str
    timestamp: date
    class ConfigDict():
        from_attributes = True
#-----------------------------------------------------------------------------