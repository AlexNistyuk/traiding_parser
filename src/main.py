from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.mongo_manager import Manager as DatabaseManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager = await DatabaseManager.connect()

    yield

    await db_manager.close()


app = FastAPI(lifespan=lifespan)
