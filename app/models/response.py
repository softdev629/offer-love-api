from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from .offer import Offer


class OfferResponse(BaseModel):
    status: str
    data: List[Offer]


class StatsResponse(BaseModel):
    offers: int
    merchants: int
    lastOfferAdded: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "offers": 150,
                "merchants": 45,
                "lastOfferAdded": "2024-12-20T09:06:37.409Z",
            }
        }

class LatestOfferImageItem(BaseModel):
    merchant_slug: str = Field(alias="merchantSlug")
    merchant_logo: str | None = Field(default=None, alias="merchantLogo")
    offer: str

    class Config:
        populate_by_name = True

class LatestOfferImagesResponse(BaseModel):
    status: str
    data: List[LatestOfferImageItem]

class MerchantOffersResponse(BaseModel):
    status: str
    data: List[Offer]

class SearchOffersResponse(BaseModel):
    status: str
    data: List[Offer]

class LatestOffersResponse(BaseModel):
    status: str
    data: List[Offer]

class SingleOfferResponse(BaseModel):
    status: str
    data: Offer

class MerchantNameItem(BaseModel):
    merchant_slug: str = Field(alias="merchantSlug")
    merchant_name: str = Field(alias="merchantName")

    class Config:
        populate_by_name = True

class MerchantNamesResponse(BaseModel):
    status: str
    data: List[MerchantNameItem]
