from pydantic import BaseModel
from typing import Optional

class Quote(BaseModel):
    quoteText:str
    quoteAuthor:str
    id:Optional[int]
