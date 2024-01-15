from fastapi import APIRouter

from assets.domain.entities import AssetCreateDTO, AssetGetDTO
from assets.use_case.assets_get import AssetGetUseCase
from assets.use_case.assets_insert import AssetInsertUseCase

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=list[AssetGetDTO])
async def get_assets() -> list[dict]:
    return await AssetGetUseCase().get_all()


@router.post("/", status_code=201, response_model=dict)
async def create_asset(asset: AssetCreateDTO) -> dict:
    result = await AssetInsertUseCase().insert_one(asset.model_dump())

    return {"_id": str(result.inserted_id)}


@router.get("/{asset_id}", response_model=AssetGetDTO)
async def get_asset(asset_id: str) -> dict:
    return await AssetGetUseCase().get_by_id(asset_id)
