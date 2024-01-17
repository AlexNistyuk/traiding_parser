from fastapi import APIRouter

from application.use_case.assets import AssetUseCase
from domain.entities.assets import AssetCreateDTO, AssetGetDTO

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=list[AssetGetDTO])
async def get_assets() -> list[dict]:
    return await AssetUseCase().get_all()


@router.post("/", status_code=201, response_model=dict)
async def create_asset(asset: AssetCreateDTO) -> dict:
    result = await AssetUseCase().insert_one(asset.model_dump())

    return {"_id": str(result.inserted_id)}


@router.get("/{asset_id}", response_model=AssetGetDTO)
async def get_asset(asset_id: str) -> dict:
    return await AssetUseCase().get_by_id(asset_id)
