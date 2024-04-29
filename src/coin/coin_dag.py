import yfinance as yf
from src.coin.coin_model import Coin, PriceHistory, MarketCap
from src.coin.coin_service import CoinService
from typing import Dict
from datetime import datetime
import asyncio

cryptocurrency_dict = {
    "Bitcoin": "BTC-USD",
    "Ethereum": "ETH-USD",
    "Tether": "USDT-USD",
    "BNB": "BNB-USD",
    "Solana": "SOL-USD",
    "USD Coin": "USDC-USD",
    "XRP": "XRP-USD",
    "Lido Staked ETH": "STETH-USD",
    "Dogecoin": "DOGE-USD",
    "Cardano": "ADA-USD",
    "Toncoin": "TON11419-USD",
    "Avalanche": "AVAX-USD",
    "Shiba Inu": "SHIB-USD",
    "Bitcoin Cash": "BCH-USD",
    "Polkadot": "DOT-USD",
    "Wrapped Bitcoin": "WBTC-USD",
    "Wrapped TRON": "WTRX-USD",
    "TRON": "TRX-USD",
    "Chainlink": "LINK-USD",
    "Polygon": "MATIC-USD"
}


async def fetch_and_store_data(symbols: Dict[str, str]):
    service = CoinService()

    for coin_name, symbol in symbols.items():
        print(f"Checking available data for {coin_name}")

        # Check the earliest data available
        try:
            early_data = yf.download(symbol, period="1d", interval="1d", end="2003-01-01")
            if not early_data.empty:
                start_date = early_data.index.min().strftime('%Y-%m-%d')
            else:
                start_date = "2014-09-17"  # A common default start date
        except Exception as e:
            print(f"Failed to fetch early data for {coin_name}: {e}")
            start_date = "2014-09-17"  # Fallback if there's an error

        print(f"Fetching data from {start_date} for {coin_name}")
        data = yf.download(symbol, start=start_date, interval="1d")
        data.reset_index(inplace=True)

        # Create a new coin entity and add to the database
        coin = Coin(name=coin_name, symbol=symbol)
        coin_id = await service.add_coin(coin)

        # Iterate through each row in the dataframe to create PriceHistory and MarketCap entries
        for index, row in data.iterrows():
            price_history = PriceHistory(
                coin_id=coin_id,
                date=row['Date'],
                price=row['Close'],
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                volume=row['Volume']
            )
            market_cap = MarketCap(
                coin_id=coin_id,
                date=row['Date'],
                market_cap=row['Close'] * row['Volume']  # Simplistic market cap calculation
            )
            await service.add_price_history(price_history)
            await service.add_market_cap(market_cap)

        print(f"Data stored for {coin_name}")


if __name__ == "__main__":
    asyncio.run(fetch_and_store_data(cryptocurrency_dict))
