from fastapi import APIRouter

router = APIRouter(prefix="/assets", tags=["assets"])

router.get("/")


async def get_assets():
    ...
