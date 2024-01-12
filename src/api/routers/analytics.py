from typing import List

from fastapi import APIRouter

from analytics.schemas import AnalyticsGet, AnalyticsHistory
from services.analytics import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/", response_model=List[AnalyticsGet])
async def get_assets():
    return await AnalyticsService().get_all()


@router.get("/history", response_model=AnalyticsHistory)
async def get_assets_history():
    return await AnalyticsService().get_group_by_assets()


@router.get("/{asset_id}", response_model=AnalyticsGet)
async def get_asset(asset_id: str):
    return await AnalyticsService().get_by_id(asset_id)
