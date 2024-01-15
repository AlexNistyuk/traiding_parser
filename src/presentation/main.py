from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from binances.infrastructure.manager import BinanceManager
from common.infrastructure.managers.mongo_manager import Manager as DatabaseManager
from presentation.api.v1.routers import router as v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager = await DatabaseManager.connect()
    binance_manager = await BinanceManager.connect()

    yield

    await db_manager.close()
    await binance_manager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(v1_router)


if __name__ == "__main__":
    uvicorn.run(app=app)
