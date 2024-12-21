from fastapi import HTTPException
from ..config.database import offers_collection
from ..models.response import LatestOfferImageItem, Offer, MerchantNameItem
from datetime import datetime

def fetch_latest_offer_images(limit: int = 8):
    try:
        latest_offers = offers_collection.find(
            {"merchantLogo": {"$ne": None}},
            projection={
                "merchantSlug": 1,
                "merchantLogo": 1,
                "offer": 1
            }
        ).sort("insertedAt", -1).limit(limit)

        return [
            LatestOfferImageItem(
                merchantSlug=offer["merchantSlug"],
                merchantLogo=offer["merchantLogo"],
                offer=offer["offer"]
            ) for offer in latest_offers
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def fetch_merchant_offers(merchant_slug: str):
    try:
        merchant_offers = offers_collection.find(
            {"merchantSlug": merchant_slug}
        ).sort("insertedAt", -1)  # Sort by newest first

        return [
            Offer(
                _id=str(offer["_id"]),
                merchantSlug=offer["merchantSlug"],
                offerSlug=offer["offerSlug"],
                merchantLogo=offer.get("merchantLogo"),
                merchantName=offer["merchantName"],
                link=offer.get("link"),
                offer=offer["offer"],
                start_date=offer.get("start_date"),
                end_date=offer.get("end_date"),
                value=offer.get("value"),
                description=offer["description"],
                bank=offer["bank"],
                insertedAt=offer["insertedAt"]
            ) for offer in merchant_offers
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def search_offers(query: str):
    try:
        # Create a case-insensitive search pattern
        search_pattern = {"$regex": query, "$options": "i"}
        
        # Search in multiple fields
        search_results = offers_collection.find({
            "$or": [
                {"offer": search_pattern},
                {"description": search_pattern},
                {"merchantName": search_pattern},
                {"merchantSlug": search_pattern}
            ]
        }).sort("insertedAt", -1)  # Sort by newest first

        return [
            Offer(
                _id=str(offer["_id"]),
                merchantSlug=offer["merchantSlug"],
                offerSlug=offer["offerSlug"],
                merchantLogo=offer.get("merchantLogo"),
                merchantName=offer["merchantName"],
                link=offer.get("link"),
                offer=offer["offer"],
                start_date=offer.get("start_date"),
                end_date=offer.get("end_date"),
                value=offer.get("value"),
                description=offer["description"],
                bank=offer["bank"],
                insertedAt=offer["insertedAt"]
            ) for offer in search_results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def fetch_latest_offers():
    try:
        latest_offers = offers_collection.find({}).sort(
            "insertedAt", -1
        )

        return [
            Offer(
                _id=str(offer["_id"]),
                merchantSlug=offer["merchantSlug"],
                offerSlug=offer["offerSlug"],
                merchantLogo=offer.get("merchantLogo"),
                merchantName=offer["merchantName"],
                link=offer.get("link"),
                offer=offer["offer"],
                start_date=offer.get("start_date"),
                end_date=offer.get("end_date"),
                value=offer.get("value"),
                description=offer["description"],
                bank=offer["bank"],
                insertedAt=offer["insertedAt"]
            ) for offer in latest_offers
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def fetch_specific_offer(merchant_slug: str, offer_slug: str, date_slug: str):
    try:
        if date_slug == "no-expiry":
            date_slug = None
            
        # Find the specific offer
        offer = offers_collection.find_one({
            "merchantSlug": merchant_slug,
            "offerSlug": offer_slug,
            "end_date": date_slug
        })

        if not offer:
            return None

        return Offer(
            _id=str(offer["_id"]),
            merchantSlug=offer["merchantSlug"],
            offerSlug=offer["offerSlug"],
            merchantLogo=offer.get("merchantLogo"),
            merchantName=offer["merchantName"],
            link=offer.get("link"),
            offer=offer["offer"],
            start_date=offer.get("start_date"),
            end_date=offer.get("end_date"),
            value=offer.get("value"),
            description=offer["description"],
            bank=offer["bank"],
            insertedAt=offer["insertedAt"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def fetch_merchant_names():
    try:
        # Use aggregation to get unique merchants with their names
        merchants = offers_collection.aggregate([
            {
                "$group": {
                    "_id": {
                        "merchantSlug": "$merchantSlug",
                        "merchantName": "$merchantName"
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "merchantSlug": "$_id.merchantSlug",
                    "merchantName": "$_id.merchantName"
                }
            },
            {
                "$sort": {"merchantName": 1},
            }
        ])

        print(merchants)

        return [
            MerchantNameItem(
                merchantSlug=merchant["merchantSlug"],
                merchantName=merchant["merchantName"]
            ) for merchant in merchants
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}") 