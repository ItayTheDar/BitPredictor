from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CoinID(BaseModel):
    id: Optional[int] = Field(..., example=1, description="Coin ID")


class Coin(BaseModel):
    name: str = Field(..., example="Bitcoin", description="Coin Name")
    symbol: str = Field(..., example="BTC", description="Coin Symbol")

    class Config:
        orm_mode = True


class PriceHistory(BaseModel):
    id: Optional[int] = Field(..., example=1, description="Record ID")
    coin_id: int = Field(..., example=1, description="Coin ID")
    date: datetime = Field(..., example="2021-01-01", description="Date")
    price: float = Field(..., example=1000.0, description="Price")
    open: float = Field(..., example=1000.0, description="Open")
    high: float = Field(..., example=1000.0, description="High")
    low: float = Field(..., example=1000.0, description="Low")
    volume: float = Field(..., example=1000.0, description="Volume")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "coin_id": 1,
                "date": "2021-01-01",
                "price": 1000.0,
                "open": 1000.0,
                "high": 1000.0,
                "low": 1000.0,
                "volume": 1000.0,
            }
        }


class MarketCap(BaseModel):
    id: Optional[int] = Field(..., example=1, description="Record ID")
    coin_id: int = Field(..., example=1, description="Coin ID")
    date: datetime = Field(..., example="2021-01-01", description="Date")
    market_cap: float = Field(..., example=1000.0, description="Market Cap")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"coin_id": 1, "date": "2021-01-01", "market_cap": 1000.0}
        }


class UpdateCoin(BaseModel):
    name: Optional[str] = Field(..., example="Bitcoin", description="Coin Name")
    symbol: Optional[str] = Field(..., example="BTC", description="Coin Symbol")

    class Config:
        schema_extra = {"example": {"name": "Bitcoin", "symbol": "BTC"}}


class UpdatePriceHistory(BaseModel):
    coin_id: Optional[int] = Field(..., example=1, description="Coin ID")
    date: Optional[datetime] = Field(..., example="2021-01-01", description="Date")
    price: Optional[float] = Field(..., example=1000.0, description="Price")
    open: Optional[float] = Field(..., example=1000.0, description="Open")
    high: Optional[float] = Field(..., example=1000.0, description="High")
    low: Optional[float] = Field(..., example=1000.0, description="Low")
    volume: Optional[float] = Field(..., example=1000.0, description="Volume")

    class Config:
        schema_extra = {
            "example": {
                "coin_id": 1,
                "date": "2021-01-01",
                "price": 1000.0,
                "open": 1000.0,
                "high": 1000.0,
                "low": 1000.0,
                "volume": 1000.0,
            }
        }


class UpdateMarketCap(BaseModel):
    coin_id: Optional[int] = Field(..., example=1, description="Coin ID")
    date: Optional[datetime] = Field(..., example="2021-01-01", description="Date")
    market_cap: Optional[float] = Field(..., example=1000.0, description="Market Cap")

    class Config:
        schema_extra = {"example": {"date": "2021-01-01", "market_cap": 1000.0}}
