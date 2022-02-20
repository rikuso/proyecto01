#cambiar los nombre luego de las funciones y el valor o parametro
def cartaEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "codigo":item["codigo"],
        "cordenada_A":item["cordenada_A"],
        "cordenada_B":item["cordenada_B"],
        "estado":item["estado"]
    }

def cartasEntity(entity)-> list:
    return [cartaEntity(item) for item in entity]

