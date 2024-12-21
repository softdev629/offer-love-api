from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB connection details
MONGO_DETAILS = os.getenv("MONGO_URI")

# Initialize MongoDB client
try:
    client = MongoClient(MONGO_DETAILS)
    client.server_info()  # will raise an exception if connection fails
    database = client.arabic
    offers_collection = database.get_collection("offers")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    raise 