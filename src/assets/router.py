from fastapi import APIRouter

from assets.schemas import AssetCreate, AssetGet, AssetHistory
from repositories.assets import AssetRepository

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/")
async def get_assets():
    documents = await AssetRepository().get_all()

    return [AssetGet.model_validate(document) for document in documents]


@router.post("/", status_code=201)
async def create_asset(asset: AssetCreate):
    result = await AssetRepository().insert_one(asset.model_dump())

    return {"id": str(result.inserted_id)}


@router.get("/history")
async def get_assets_history():
    documents = await AssetRepository().get_group_by_assets()

    return [AssetHistory.model_validate(document) for document in documents]


@router.get("/{asset_id}")
async def get_asset(asset_id: str):
    document = await AssetRepository().get_by_id(asset_id)

    return AssetGet.model_validate(document)
