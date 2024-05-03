from nest.core import Controller, Get, Post, Put, Delete

from .coin_service import CoinService
from .coin_model import (
    Coin,
    PriceHistory,
    MarketCap,
    UpdateCoin,
)


@Controller("coin")
class CoinController:
    def __init__(
            self,
            service: CoinService = CoinService,
    ):
        self.service = service

    ## CRUD for coin resource
    @Get("/")
    async def get_coins(self):
        return await self.service.get_coin()

    @Post("/")
    async def add_coin(self, coin: Coin):
        return await self.service.add_coin(coin)

    @Put("/{coin_id}")
    async def update_coin(self, coin_id: int, coin: UpdateCoin):
        return await self.service.update_coin(coin_id, coin)

    @Delete("/{coin_id}")
    async def delete_coin(self, coin_id: int):
        return await self.service.delete_coin(coin_id)

    @Get("/{coin_id}")
    async def get_coin_by_id(self, coin_id: int):
        return await self.service.get_coin_by_id(coin_id)

    @Get("/get_coin_by_name/{coin_name}")
    async def get_coin_by_name(self, coin_name: str):
        return await self.service.get_coin_by_name(coin_name)

    ## PriceHistory CRUD Operations

    @Get("/get_price_history/{coin_id}")
    async def get_price_history(self, coin_id: int):
        return await self.service.get_price_history(coin_id)

    @Get("/get_market_cap/{coin_id}")
    async def get_market_cap(self, coin_id: int):
        return await self.service.get_market_cap(coin_id)

    @Post("/add_price_history/")
    async def add_price_history(self, price_history: PriceHistory):
        return await self.service.add_price_history(price_history)

    @Post("/add_market_cap/")
    async def add_market_cap(self, market_cap: MarketCap):
        return await self.service.add_market_cap(market_cap)

    @Get("/get_coin_last_update/{symbol}")
    async def get_coin_last_update(self, symbol: str):
        return await self.service.get_coin_last_update(symbol)

    @Get("/perform_query/{query}")
    async def perform_query(self, query: str):
        return await self.service.perform_query(query)
