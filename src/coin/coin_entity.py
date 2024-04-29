from src.config import config
from sqlalchemy import Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Coin(config.Base):
    __tablename__ = "coins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    symbol: Mapped[str] = mapped_column(String, unique=True)

    price_history = relationship("PriceHistory", back_populates="coin")
    market_cap = relationship("MarketCap", back_populates="coin")


class PriceHistory(config.Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    coin_id: Mapped[int] = mapped_column(Integer, ForeignKey("coins.id"))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    price: Mapped[float] = mapped_column(Float)
    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    coin = relationship("Coin", back_populates="price_history")  # Corrected relationship attribute


class MarketCap(config.Base):
    __tablename__ = "market_cap"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    coin_id: Mapped[int] = mapped_column(Integer, ForeignKey("coins.id"))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    market_cap: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    coin = relationship("Coin", back_populates="market_cap")  # Corrected relationship attribute
