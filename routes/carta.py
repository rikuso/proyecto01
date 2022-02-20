from fastapi import APIRouter, Response,status
from config.db import conn, card
from schemas.carta import cartaEntity, cartasEntity, usuarioEntity, usuariosEntity
from models.carta import Card, Usuario
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

# Agregar cartas
#============================================================
#METODO POST PARA CARTA Y USUARIO
#============================================================

@user.post('/users')
def create_user(user: Usuario):
    new_carta = dict(user)

    del new_carta["id"]

    id = conn.yugioh.user.insert_one(new_carta).inserted_id
    user = conn.yugioh.user.find_one({"_id": id})

    return usuarioEntity(user)

@user.post('/cards')
def create_carta(user: Card):
    new_carta = dict(user)

    del new_carta["id"]

    id = conn.yugioh.card.insert_one(new_carta).inserted_id
    card = conn.yugioh.card.find_one({"_id": id})

    return cartaEntity(card)



# Traer todas las cartas
#===================================================
#METODO PARA TRAER TODAS LAS CARTA O USUARIOS
#===================================================
@user.get('/users')
def consultar_todas():
    return usuariosEntity(conn.yugioh.user.find())

@user.get('/cards')
def consultar_todas():
    return cartasEntity(conn.yugioh.card.find())

# Traer una carta
#==================================================
#METODO PARA TRAER UNA CARTA O UN USUARIO POR MEDIO
#                   ID
#=================================================

@user.get('/users/{id}')
def consulta_una(id: str):
    return usuarioEntity(conn.yugioh.user.find_one({"_id": ObjectId(id)}))

@user.get('/cards/{id}')
def consulta_una(id: str):
    return cartaEntity(conn.yugioh.card.find_one({"_id": ObjectId(id)}))
#=================================================
#               CODIGO O NOMBRE
#=================================================
@user.get('/users/{name}')
def consulta_una(name: str):
    return usuarioEntity(conn.yugioh.user.find_one({"name": name}))

@user.get('/cards/{codigo}')
def consulta_una(codigo: str):
    return cartaEntity(conn.yugioh.card.find_one({"codigo": codigo}))

# Editar una Carta o posicion
#================================================
#METODO PARA EDITAR LA CARTA ID O CODIGO
#================================================

@user.put('/cards/{id}')
def update_card(id: str, user: Card):
    conn.yugioh.card.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return usuarioEntity(conn.yugioh.card.find_one({"_id": ObjectId(id)}))

@user.put('/cards/{codigo}')
def update_card(codigo: str, user: Card):
    conn.yugioh.card.find_one_and_update(
        {"codigo":codigo}, {"$set": dict(user)})
    return cartaEntity(conn.yugioh.card.find_one({"codigo":codigo}))

# Eliminar una carta
#==============================================
#METODO PARA ELIMINAR UNA CARTA CON CODIGO O ID
#==============================================

@user.delete('/cards/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_card(id: str):
    usuarioEntity(conn.yugioh.card.find_one_and_delete({"_id": ObjectId(id)}))

    return Response(status_code=HTTP_204_NO_CONTENT)

@user.delete('/cards/{codigo}',status_code=status.HTTP_204_NO_CONTENT)
def delete_card(codigo: str):
    cartaEntity(conn.yugioh.card.find_one_and_delete({"codigo":codigo}))

    return Response(status_code=HTTP_204_NO_CONTENT)
