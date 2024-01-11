from typing import List

from fastapi import APIRouter

from assets.schemas import AssetCreate, AssetGet, AssetHistory
from services.assets import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=List[AssetGet])
async def get_assets():
    return await AssetService().get_all()


@router.post("/", status_code=201, response_model=dict)
async def create_asset(asset: AssetCreate):
    result = await AssetService().insert_one(asset.model_dump())

    return {"id": str(result.inserted_id)}


@router.get("/history", response_model=List[AssetHistory])
async def get_assets_history():
    return await AssetService().get_group_by_assets()


@router.get("/{asset_id}", response_model=AssetGet)
async def get_asset(asset_id: str):
    return await AssetService().get_by_id(asset_id)
