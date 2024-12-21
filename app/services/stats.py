from fastapi import HTTPException
from ..config.database import offers_collection

def fetch_stats():
    try:
        total_offers = offers_collection.count_documents({})
        total_merchants = len(offers_collection.distinct("merchantSlug"))
        latest_offer = offers_collection.find_one(sort=[("insertedAt", -1)])
        latest_offer_added = latest_offer["insertedAt"] if latest_offer else None

        return {
            "offers": total_offers,
            "merchants": total_merchants,
            "lastOfferAdded": latest_offer_added
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}") 