from fastapi import FastAPI, HTTPException  
from pymongo import MongoClient  
from typing import List  
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()  

# MongoDB connection details  
MONGO_DETAILS = os.getenv("MONGO_URI")

# Initialize MongoDB client  
client = MongoClient(MONGO_DETAILS)  
database = client.arabic  
offers_collection = database.get_collection("offers")  

# Pydantic model for Offer  
class Offer(BaseModel):  
    id: str  
    title: str  
    link: str
    start_date: str | None
    end_date: str | None
    value: int | None
    description: str

def fetch_offers():  
    offers_cursor = offers_collection.find({})  
    offers = []  
    for offer in offers_cursor:  
        offers.append(Offer(id=str(offer["_id"]), title=offer["title"], description=offer["description"], link=offer["link"], start_date=offer["start_date"], end_date=offer["end_date"], value=offer["value"]))  
    return offers

@app.get("/api/offers")  
def get_offers():  
    offers = fetch_offers()  
    if not offers:  
        raise HTTPException(status_code=404, detail="No offers found")  
    return {"status": "success", "data": offers}