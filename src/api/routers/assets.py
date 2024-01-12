from typing import List

from fastapi import APIRouter

from assets.schemas import AssetCreate, AssetGet
from services.assets import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=List[AssetGet])
async def get_assets() -> list[dict]:
    return await AssetService().get_all()


@router.post("/", status_code=201, response_model=dict)
async def create_asset(asset: AssetCreate) -> dict:
    result = await AssetService().insert_one(asset.model_dump())

    return {"id": str(result.inserted_id)}


@router.get("/{asset_id}", response_model=AssetGet)
async def get_asset(asset_id: str) -> dict:
    return await AssetService().get_by_id(asset_id)
