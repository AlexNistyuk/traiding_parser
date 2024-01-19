from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from application.use_case.coins import CoinUseCase

router = APIRouter(prefix="/coins", tags=["Update coins"])


@router.get("/update", status_code=HTTP_200_OK)
async def update_coins():
    try:
        await CoinUseCase().get_data_and_send()

        return JSONResponse({"detail": "successfully"})
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )
