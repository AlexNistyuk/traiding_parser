from fastapi import APIRouter

from analytics.domain.entities import AnalyticsGetDTO, AnalyticsHistoryDTO
from analytics.use_case.analytics_get import AnalyticsGetUseCase

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/", response_model=list[AnalyticsGetDTO])
async def get_assets() -> list[dict]:
    return await AnalyticsGetUseCase().get_all()


@router.get("/history", response_model=AnalyticsHistoryDTO)
async def get_assets_history() -> dict:
    return await AnalyticsGetUseCase().get_group_by_assets()


@router.get("/{asset_id}", response_model=AnalyticsGetDTO)
async def get_asset(asset_id: str) -> dict:
    return await AnalyticsGetUseCase().get_by_id(asset_id)
