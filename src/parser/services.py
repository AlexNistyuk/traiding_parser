from binance import AsyncClient


class BinanceAPIService:
    async def __aenter__(self):
        self.client = await AsyncClient.create()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.close_connection()

    async def get_all_tickers(self) -> map:
        tickers = await self.client.get_all_tickers()

        return map(self.__convert_price_to_float, tickers)

    def __convert_price_to_float(self, value: dict):
        value["price"] = float(value["price"])

        return value
