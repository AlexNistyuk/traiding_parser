from contextlib import asynccontextmanager
from parser.manager import BinanceManager

import uvicorn
from fastapi import FastAPI

from assets.router import router as assets_router
from db.mongo_manager import Manager as DatabaseManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager = await DatabaseManager.connect()
    binance_manager = await BinanceManager.connect()

    yield

    await db_manager.close()
    await binance_manager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(assets_router)


if __name__ == "__main__":
    uvicorn.run(app=app)
