from fastapi import APIRouter
from ..models.response import StatsResponse
from ..services.stats import fetch_stats

router = APIRouter()

@router.get("/stats", response_model=StatsResponse)
def get_stats():
    stats = fetch_stats()
    return stats