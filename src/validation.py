
from pydantic import BaseModel


class Register(BaseModel):
     name: str
     password: str
     
     

class NameUp(BaseModel):
     your_id: int
     new_name: str
     password: str