import logging

from binance.exceptions import BinanceWebsocketUnableToConnect
from binance.streams import BinanceSocketManager, ReconnectingWebsocket

from binance import AsyncClient

logger = logging.Logger(__name__)


class BinanceManager:
    client: AsyncClient
    web_socket: ReconnectingWebsocket

    @classmethod
    async def connect(cls):
        try:
            logger.info("Connect to Binance API using web socket")

            cls.client = await AsyncClient.create()
            cls.web_socket = BinanceSocketManager(cls.client).ticker_socket()

            await cls.web_socket.connect()

            return cls
        except BinanceWebsocketUnableToConnect as exc:
            logger.error(f"Error while connecting to binance api: {exc}")

    @classmethod
    async def close(cls):
        await cls.client.close_connection()

        logger.info("Close Binance API web socker connection")
