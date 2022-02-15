from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    
    id : Optional[str]
    codigo : str
    posicion : str
    estado : bool
