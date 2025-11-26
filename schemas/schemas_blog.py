from pydantic import BaseModel

#-----------------------------------------------------------------------------
class BlogBase(BaseModel):      # data that we will receive from the user
    creator: str
    title: str
    content: str

class blogDisplay(BaseModel):   # data that we will send back to the user                                   
    creator: str                # sends back only username and email in
    title: str                  # the response body in the docs
    content: str
    class ConfigDict():
        from_attributes = True
#-----------------------------------------------------------------------------