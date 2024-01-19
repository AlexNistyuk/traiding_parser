from fastapi import APIRouter, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from application.use_case.coins import CoinUseCase

router = APIRouter(prefix="/coins", tags=["Update coins"])


@router.get("/update")
async def update_coins():
    try:
        await CoinUseCase().get_data_and_send()

        return Response(content="successfully", status_code=HTTP_200_OK)
    except Exception as exc:
        raise HTTPException(
            detail={"error": str(exc)}, status_code=HTTP_400_BAD_REQUEST
        )
