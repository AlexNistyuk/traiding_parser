from fastapi import APIRouter

from analytics.presentation.api.v1.routers import router as analytics_router
from assets.presentation.api.v1.routers import router as asset_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(asset_router)
router.include_router(analytics_router)
