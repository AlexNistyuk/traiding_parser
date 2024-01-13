from fastapi import APIRouter

from api.routers.analytics import router as analytics_router
from api.routers.assets import router as asset_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(asset_router)
router.include_router(analytics_router)
