from fastapi import APIRouter

from domain.entities.analytics import AnalyticsGetDTO, AnalyticsHistoryDTO
from use_case.analytics import AnalyticsUseCase

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/", response_model=list[AnalyticsGetDTO])
async def get_assets() -> list[dict]:
    return await AnalyticsUseCase().get_all()


@router.get("/history", response_model=AnalyticsHistoryDTO)
async def get_assets_history() -> dict:
    return await AnalyticsUseCase().get_group_by_assets()


@router.get("/{asset_id}", response_model=AnalyticsGetDTO)
async def get_asset(asset_id: str) -> dict:
    return await AnalyticsUseCase().get_by_id(asset_id)
