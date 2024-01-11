from fastapi import APIRouter

from api.routers.assets import router as asset_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(asset_router)
