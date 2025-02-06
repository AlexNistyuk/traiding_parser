import logging

from binance import AsyncClient
from binance.exceptions import BinanceWebsocketUnableToConnect
from binance.streams import BinanceSocketManager, ReconnectingWebsocket

from infrastructure.config import get_settings
from infrastructure.managers.interfaces import IManager

logger = logging.Logger(__name__)


class BinanceManager(IManager):
    client: AsyncClient
    web_socket: ReconnectingWebsocket

    @classmethod
    async def connect(cls):
        try:
            logger.info("Connect to Binance API using web socket")

            AsyncClient.REQUEST_TIMEOUT = get_settings().binance_api_request_timeout
            cls.client = await AsyncClient.create()
            cls.web_socket = BinanceSocketManager(cls.client).ticker_socket()

            await cls.web_socket.__aenter__()

            return cls
        except BinanceWebsocketUnableToConnect as exc:
            logger.error(f"Error while connecting to Binance API: {exc}")

    @classmethod
    async def close(cls) -> None:
        await cls.web_socket.__aexit__(None, None, None)
        await cls.client.close_connection()

        logger.info("Close Binance API web socket connection")
