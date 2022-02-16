#cambiar los nombre luego de las funciones y el valor o parametro
def cartaEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "codigo":item["codigo"],
        "posicion":item["posicion"],
        "coordenada":item["coordenada"],
        "estado":item["estado"]
    }

def cartasEntity(entity)-> list:
    return [cartaEntity(item) for item in entity]
