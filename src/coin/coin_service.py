from .coin_model import (
    Coin,
    PriceHistory,
    MarketCap,
)
from .coin_entity import (
    Coin as CoinEntity,
    PriceHistory as PriceHistoryEntity,
    MarketCap as MarketCapEntity,
)
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable
from src.config import config

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


@Injectable
class CoinService:
    
    def __init__(self):
        self.session = config.session
        
    @async_db_request_handler
    async def add_coin(self, coin: Coin):
        async with self.session() as session:
            new_coin = CoinEntity(**coin.dict())
            session.add(new_coin)
            await session.commit()
            return new_coin.id

    @async_db_request_handler
    async def get_coins(self):
        async with self.session() as session:
            query = select(CoinEntity)
            result = await session.execute(query)
            return result.scalars().all()

    @async_db_request_handler
    async def get_coin_by_id(self, coin_id: int):
        async with self.session() as session:
            query = select(CoinEntity).where(CoinEntity.id == coin_id)
            result = await session.execute(query)
            return result.scalars().first()

    @async_db_request_handler
    async def get_coin_by_name(self, coin_name: str):
        async with self.session() as session:
            query = select(CoinEntity).where(CoinEntity.name == coin_name)
            result = await session.execute(query)
            return result.scalars().first()

    @async_db_request_handler
    async def add_price_history(
        self, price_history: PriceHistory
    ):
        async with self.session() as session:
            new_price_history = PriceHistoryEntity(**price_history.dict())
            session.add(new_price_history)
            await session.commit()
        return new_price_history.id

    @async_db_request_handler
    async def get_price_history(self, coin_id: int):
        async with self.session() as session:
            query = select(PriceHistoryEntity).where(PriceHistoryEntity.coin_id == coin_id)
            result = await session.execute(query)
            return result.scalars().all()

    @async_db_request_handler
    async def add_market_cap(self, market_cap: MarketCap):
        async with self.session() as session:
            new_market_cap = MarketCapEntity(**market_cap.dict())
            session.add(new_market_cap)
            await session.commit()
        return new_market_cap.id

    @async_db_request_handler
    async def get_market_cap(self, coin_id: int):
        async with self.session() as session:
            query = select(MarketCapEntity).where(MarketCapEntity.coin_id == coin_id)
            result = await session.execute(query)
        return result.scalars().all()
