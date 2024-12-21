from fastapi import APIRouter, HTTPException
from ..models.response import (
    LatestOfferImagesResponse,
    MerchantOffersResponse,
    SearchOffersResponse,
    LatestOffersResponse,
    SingleOfferResponse,
    MerchantNamesResponse,
)
from ..services.offer import (
    fetch_latest_offer_images,
    fetch_merchant_offers,
    search_offers,
    fetch_latest_offers,
    fetch_specific_offer,
    fetch_merchant_names,
)

router = APIRouter()


@router.get("/offer/latest-images", response_model=LatestOfferImagesResponse)
def get_latest_offer_images():
    """
    Get latest offers with images for carousel/banner display, limited to 8 items
    """
    offers = fetch_latest_offer_images()
    if not offers:
        raise HTTPException(status_code=404, detail="No offers found")
    return {"status": "success", "data": offers}


@router.get("/offer/search", response_model=SearchOffersResponse)
def search_offers_route(q: str):
    """
    Search offers by query string. Searches in offer titles, descriptions, and merchant names.
    """
    if len(q.strip()) < 2:
        raise HTTPException(
            status_code=400, detail="Search query must be at least 2 characters long"
        )

    offers = search_offers(q)
    if not offers:
        raise HTTPException(status_code=404, detail=f"No offers found for query: {q}")
    return {"status": "success", "data": offers}


@router.get("/offer/latest", response_model=LatestOffersResponse)
def get_latest_offers():
    """
    Get latest offers sorted by insertion date
    """

    offers = fetch_latest_offers()
    if not offers:
        raise HTTPException(status_code=404, detail="No offers found")
    return {"status": "success", "data": offers}


@router.get("/offer/merchants", response_model=MerchantNamesResponse)
def get_merchant_names():
    """
    Get list of all unique merchants sorted alphabetically by name
    """
    merchants = fetch_merchant_names()
    if not merchants:
        raise HTTPException(status_code=404, detail="No merchants found")
    return {"status": "success", "data": merchants}


@router.get("/offer/{merchant_slug}", response_model=MerchantOffersResponse)
def get_merchant_offers(merchant_slug: str):
    """
    Get all offers for a specific merchant by their merchant slug
    """
    offers = fetch_merchant_offers(merchant_slug)
    if not offers:
        raise HTTPException(
            status_code=404, detail=f"No offers found for merchant: {merchant_slug}"
        )
    return {"status": "success", "data": offers}


@router.get(
    "/offer/{merchant_slug}/{offer_slug}/{date_slug}",
    response_model=SingleOfferResponse,
)
def get_specific_offer(merchant_slug: str, offer_slug: str, date_slug: str):
    """
    Get a specific offer by merchant slug, offer slug, and end date
    Date format should be YYYY-MM-DD
    """
    offer = fetch_specific_offer(merchant_slug, offer_slug, date_slug)
    if not offer:
        raise HTTPException(
            status_code=404, detail=f"No offer found with the specified parameters"
        )
    return {"status": "success", "data": offer}