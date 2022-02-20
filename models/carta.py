from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    
    id : Optional[str]
    codigo : str
    posicion : str
    cordenada_A: str
    cordenada_B: str
    estado : str

