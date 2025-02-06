from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from application.use_case.assets import AssetUseCase
from domain.entities.assets import AssetCreateDTO, AssetGetDTO

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=list[AssetGetDTO], status_code=HTTP_200_OK)
async def get_assets() -> list[dict]:
    try:
        return await AssetUseCase().get_all()
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )


@router.post("/", response_model=dict, status_code=HTTP_201_CREATED)
async def create_asset(asset: AssetCreateDTO) -> dict:
    try:
        result = await AssetUseCase().insert_one(asset.model_dump())

        return {"_id": str(result.inserted_id)}
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )


@router.get("/{asset_id}", response_model=AssetGetDTO, status_code=HTTP_200_OK)
async def get_asset(asset_id: str) -> dict:
    try:
        return await AssetUseCase().get_by_id(asset_id)
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )
