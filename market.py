import yfinance as yf


def get_price(symbol: str) -> float:
    ticker = yf.Ticker(symbol)
    price = ticker.info.get("regularMarketPrice")
    if price is None:
        raise ValueError(f"No price for {symbol}")
    return float(price)
