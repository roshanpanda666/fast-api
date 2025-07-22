
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.xgo30b6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)

db = client["pydb"]
collection = db["data"]

print(username,password)