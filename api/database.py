import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
#from bson import ObjectId

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
RANDOM_N =os.getenv("RANDOM_N")

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

db = client.fastapi
col = db.hotels9ja