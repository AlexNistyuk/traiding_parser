from parser.manager import BinanceManager


class BinanceAPIService(BinanceManager):
    """Binance service. Use for getting info about tickers"""

    async def get_tickers_info(self):
        return await self.web_socket.recv()
