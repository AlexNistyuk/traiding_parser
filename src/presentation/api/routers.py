from fastapi import APIRouter

from presentation.api.v1.analytics import router as analytics_router
from presentation.api.v1.assets import router as asset_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(asset_router)
router.include_router(analytics_router)
