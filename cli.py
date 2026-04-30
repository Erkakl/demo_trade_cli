from portfolio import Portfolio
from market import get_price
from storage import init_db, get_cash

from rich import print


class CLI:

    def __init__(self):
        init_db()
        self.portfolio = Portfolio()

    def run(self):
        print("[bold green]Demo Trade CLI (Paper Trading)[/bold green]")
        print("Start balance: $10,000")
        print("Commands: /portfolio /buy /sell /price /quit")

        while True:
            try:
                cmd = input("\n> ").strip().split()

                if not cmd:
                    continue

                action = cmd[0]

                # EXIT
                if action == "/quit" or action == "QUIT67":
                    print("Exiting...")
                    break

                # PRICE
                elif action == "/price":
                    if len(cmd) < 2:
                        print("Usage: /price SYMBOL")
                        continue

                    price = get_price(cmd[1])
                    print(f"{cmd[1]} price: {price}")

                # BUY
                elif action == "/buy":
                    if len(cmd) < 3:
                        print("Usage: /buy SYMBOL QTY")
                        continue

                    symbol = cmd[1]

                    try:
                        qty = float(cmd[2])
                    except ValueError:
                        print("Quantity must be a number")
                        continue

                    price = self.portfolio.buy(symbol, qty)
                    print(f"Bought {qty} {symbol} @ {price}")

                # SELL
                elif action == "/sell":
                    if len(cmd) < 3:
                        print("Usage: /sell SYMBOL QTY")
                        continue

                    symbol = cmd[1]

                    try:
                        qty = float(cmd[2])
                    except ValueError:
                        print("Quantity must be a number")
                        continue

                    price = self.portfolio.sell(symbol, qty)
                    print(f"Sold {qty} {symbol} @ {price}")

                # PORTFOLIO
                elif action == "/portfolio":
                    data = self.portfolio.get_all()
                    cash = get_cash()

                    print("\n[bold cyan]Portfolio Overview[/bold cyan]")
                    print(f"Cash: ${cash:.2f}")

                    total = cash

                    if not data:
                        print("No positions yet")
                        print(f"\nTotal value: ${cash:.2f}")
                        continue

                    for s, q, avg in data:
                        price = get_price(s)
                        value = price * q
                        pnl = (price - avg) * q
                        total += value

                        print(
                            f"{s}: {q} shares | avg {avg:.2f} | "
                            f"value {value:.2f} | PnL {pnl:.2f}"
                        )

                    print(f"\nTotal portfolio value: ${total:.2f}")

                else:
                    print("Unknown command. Try /portfolio /buy /sell /price /quit")

            except Exception as e:
                print(f"[red]Error:[/red] {e}")
