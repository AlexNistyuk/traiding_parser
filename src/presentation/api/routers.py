from fastapi import APIRouter

from presentation.api.v1.analytics import router as analytics_router
from presentation.api.v1.assets import router as assets_router
from presentation.api.v1.coins import router as coins_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(assets_router)
router.include_router(analytics_router)
router.include_router(coins_router)
