from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    
    id : Optional[str]
    codigo : str
    cordenada_A: str
    cordenada_B: str
    estado : str

