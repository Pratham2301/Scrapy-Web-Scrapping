from pymongo import MongoClient
import datetime
import certifi
ca = certifi.where()


client = MongoClient("mongodb+srv://prathamrajbhoj2003:RL555CiQeO6QMlJ5@scrapy-tutorial.edrnmzb.mongodb.net/", tlsCAFile=ca)

db = client.testDB
collection = db.testCollection

data = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

id = collection.insert_one(data).inserted_id
print("id : ", id)