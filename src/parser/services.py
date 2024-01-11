from parser.manager import BinanceManager


class BinanceAPIService(BinanceManager):
    """Binance service. Use for getting info about tickers"""

    async def get_tickers_info(self):
        tickers = await self.web_socket.recv()

        return [self.__get_ticker_info(ticker) for ticker in tickers]

    def __get_ticker_info(self, ticker: dict):
        return {
            "symbol": ticker["s"],
            "price_change": float(ticker["p"]),
            "price_change_percent": float(ticker["P"]),
            "current_close_price": float(ticker["c"]),
            "previous_close_price": float(ticker["x"]),
            "open_price": float(ticker["o"]),
            "best_bid_price": float(ticker["b"]),
            "high_price": float(ticker["h"]),
            "low_price": float(ticker["l"]),
            "time": ticker["E"],
        }
