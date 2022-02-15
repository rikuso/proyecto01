from fastapi import APIRouter, Response,status
from config.db import conn, card
from schemas.carta import cartaEntity, cartasEntity
from models.carta import Card
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

# Agregar cartas


@user.post('/users')
def create_carta(user: Card):
    new_carta = dict(user)

    del new_carta["id"]

    id = conn.yugioh.card.insert_one(new_carta).inserted_id
    card = conn.yugioh.card.find_one({"_id": id})

    return cartaEntity(card)

# Traer todas las cartas


@user.get('/users')
def consultar_todas():
    return cartasEntity(conn.yugioh.card.find())

# Traer una carta


@user.get('/users/{id}')
def consulta_una(id: str):
    return cartaEntity(conn.yugioh.card.find_one({"_id": ObjectId(id)}))

# Editar una Carta o posicion


@user.put('/users/{id}')
def update_card(id: str, user: Card):
    conn.yugioh.card.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return cartaEntity(conn.yugioh.card.find_one({"_id": ObjectId(id)}))

# Eliminar una carta


@user.delete('/users/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_card(id: str):
    cartaEntity(conn.yugioh.card.find_one_and_delete({"_id": ObjectId(id)}))

    return Response(status_code=HTTP_204_NO_CONTENT)
