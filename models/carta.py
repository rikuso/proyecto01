from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    
    id : Optional[str]
    codigo : str
    posicion : str
    coordenada_A: str
    coordenada_B: str
    estado : str

class Usuario(BaseModel):

    id: Optional[str]
    name: str
    jugadas: float
    victorias: float