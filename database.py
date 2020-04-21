import pymongo

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0-by1uo.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database('project')
mp_data = db.mpdata
scroll_data = db.scroll
user_data = db.user



