from storage import (
    load_positions,
    upsert_position,
    get_cash,
    update_cash,
    log_trade
)

from market import get_price


class Portfolio:

    def get_all(self):
        return load_positions()

    def buy(self, symbol: str, qty: float):
        price = get_price(symbol)
        cost = price * qty

        cash = get_cash()
        if cash < cost:
            raise ValueError("Not enough cash")

        positions = dict(load_positions())

        if symbol in positions:
            old_qty, old_avg = positions[symbol]
            new_qty = old_qty + qty
            new_avg = ((old_qty * old_avg) + (qty * price)) / new_qty
        else:
            new_qty = qty
            new_avg = price

        upsert_position(symbol, new_qty, new_avg)
        update_cash(cash - cost)
        log_trade(symbol, "BUY", qty, price)

        return price

    def sell(self, symbol: str, qty: float):
        price = get_price(symbol)
        revenue = price * qty

        positions = dict(load_positions())

        if symbol not in positions:
            raise ValueError("No position")

        old_qty, avg = positions[symbol]

        if qty > old_qty:
            raise ValueError("Not enough shares")

        new_qty = old_qty - qty
        upsert_position(symbol, new_qty, avg)

        cash = get_cash()
        update_cash(cash + revenue)

        log_trade(symbol, "SELL", qty, price)

        return price
