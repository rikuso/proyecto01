from pymongo import MongoClient

conn = MongoClient("mongodb+srv://daniel:barcelona10@cluster0.6nfsz.mongodb.net/yugioh?retryWrites=true&w=majority")
db = conn.yugioh

#coleccion

card = db.carta


