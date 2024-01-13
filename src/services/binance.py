from parser.manager import BinanceManager

from bson import Decimal128


class BinanceAPIService(BinanceManager):
    """Binance service. Use for getting info about tickers"""

    async def get_tickers_info(self) -> list:
        tickers = await self.web_socket.recv()

        return [self.__get_ticker_info(ticker) for ticker in tickers]

    def __get_ticker_info(self, ticker: dict) -> dict:
        return {
            "symbol": ticker["s"],
            "price_change": Decimal128(ticker["p"]),
            "price_change_percent": Decimal128(ticker["P"]),
            "current_close_price": Decimal128(ticker["c"]),
            "previous_close_price": Decimal128(ticker["x"]),
            "open_price": Decimal128(ticker["o"]),
            "best_bid_price": Decimal128(ticker["b"]),
            "high_price": Decimal128(ticker["h"]),
            "low_price": Decimal128(ticker["l"]),
            "time": ticker["E"],
        }
