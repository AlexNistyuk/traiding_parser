from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from application.use_case.analytics import AnalyticsUseCase
from domain.entities.analytics import AnalyticsGetDTO, AnalyticsHistoryDTO

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/", response_model=list[AnalyticsGetDTO], status_code=HTTP_200_OK)
async def get_assets() -> list[dict]:
    try:
        return await AnalyticsUseCase().get_all()
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )


@router.get(
    "/history", response_model=list[AnalyticsHistoryDTO], status_code=HTTP_200_OK
)
async def get_assets_history() -> dict:
    try:
        return await AnalyticsUseCase().get_group_by_assets()
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )


@router.get("/{asset_id}", response_model=AnalyticsGetDTO, status_code=HTTP_200_OK)
async def get_asset(asset_id: str) -> dict:
    try:
        return await AnalyticsUseCase().get_by_id(asset_id)
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )
