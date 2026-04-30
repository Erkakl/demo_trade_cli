from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    quantity: float
    avg_price: float


@dataclass
class Trade:
    symbol: str
    quantity: float
    price: float
    side: str  # buy / sell
