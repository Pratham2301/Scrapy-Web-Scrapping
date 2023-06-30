from pymongo import MongoClient
import datetime
import certifi
ca = certifi.where()
import os
from dotenv import load_dotenv
load_dotenv()



DB_URL = os.getenv('DB_URL')
client = MongoClient(DB_URL, tlsCAFile=ca)


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