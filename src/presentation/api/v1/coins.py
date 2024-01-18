from fastapi import APIRouter

from application.use_case.coins import CoinUseCase

router = APIRouter(prefix="/coins", tags=["Update coins"])


@router.get("/update", response_model=dict)
async def update_coins():
    await CoinUseCase().get_data_and_send()

    return {"detail": "successfully"}
