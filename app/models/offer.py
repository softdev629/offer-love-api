from pydantic import BaseModel, Field
from datetime import datetime

class Offer(BaseModel):
    id: str = Field(alias="_id")
    merchant_slug: str = Field(alias="merchantSlug")
    offer_slug: str = Field(alias="offerSlug")
    merchant_logo: str | None = Field(default=None, alias="merchantLogo")
    merchant_name: str = Field(alias="merchantName")
    link: str | None = None
    offer: str
    start_date: str | None = Field(default=None, description="Start date of the offer")
    end_date: str | None = Field(default=None, description="End date of the offer")
    value: int | None = Field(default=None, description="Value of the offer")
    description: str
    bank: str
    inserted_at: datetime = Field(alias="insertedAt")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "6765339dcc37eb4f2cb95496",
                "merchantSlug": "ward-restaurant",
                "offerSlug": "enjoy-10%-discount",
                "merchantLogo": "https://anb.com.sa/documents/55607/3724008/ward%20logo.jpg/b3351fef-c95e-f820-8f74-ac18fe341d74",
                "merchantName": "WARD restaurant",
                "link": None,
                "offer": "Enjoy 10% discount",
                "start_date": "2024-11-15",
                "end_date": "2025-05-14",
                "value": 10,
                "description": "Enjoy 10% discount at WARD restaurant...",
                "bank": "anb",
                "insertedAt": "2024-12-20T09:06:37.409Z"
            }
        } 