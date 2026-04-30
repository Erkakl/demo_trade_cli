# demo_trade_cli

A lightweight **paper trading terminal simulator** built in Python.

It allows you to simulate buying and selling assets using live market data and track your portfolio performance in real time.

No brokers. No real money. Just market logic.

---

## ⚡ Features
- 💰 Starting cash: $10,000- 💰 Starting cash: $10,000
- 📈 Live market prices (Yahoo Finance)
- 💼 Portfolio tracking (positions + PnL)
- 🧠 Average cost basis calculation
- 💰 Buy / Sell simulation
- 📊 Real-time portfolio valuation
- 🗄 SQLite storage (persistent portfolio)
- 💬 Interactive CLI interface

---

## ⚙️ How it works

- You start with **$10,000 cash**
- Buying assets reduces cash
- Selling assets increases cash
- Portfolio value = cash + holdings
- PnL is calculated in real time using live prices

---

## 🧾 Commands

| Command            | Description                         |
|--------------------|-------------------------------------|
| `/price AAPL`      | Get live asset price                |
| `/buy AAPL 5`      | Buy 5 shares                        |
| `/sell AAPL 2`     | Sell 2 shares                       |
| `/portfolio`       | Show cash, holdings, total value    |
| `/quit`            | Exit program                        |
| `QUIT67`           | Alternative exit command            |
---

## 🚀 Run project

```bash
pip install -r requirements.txt
python main.py

## 📂 Project structure
demo_trade_cli/
├── main.py              # Entry point
├── cli.py               # CLI engine
├── portfolio.py         # Portfolio logic
├── market.py            # Market data (yfinance)
├── storage.py           # SQLite persistence
├── models.py            # Data models
│
├── db/
│   └── schema.sql       # Database schema
│
├── requirements.txt
└── README.md
🗄 Database schema
CREATE TABLE positions (
    symbol TEXT PRIMARY KEY,
    quantity REAL,
    avg_price REAL
);
```
📊 Example usage
```
> /buy AAPL 10
Bought 10 AAPL @ 170.45

> /portfolio

Portfolio Overview
Cash: $8295.50

AAPL: 10 shares | avg 168.10 | value 1704.50 | PnL +23.50

Total portfolio value: $9999.00
```
## 🧠 Design philosophy

This project focuses on:
simplicity over complexity
explainable financial logic
modular architecture
extensibility (Postgres / web dashboard ready)
## ⚠️ Limitations
No real broker integration
No order book simulation
No slippage / fees modeling
Prices are delayed (API limitation)
🔮 Future improvements
📊 Portfolio risk scoring (integrate risk engine)
📉 Charts (equity curve, drawdown)
🌐 FastAPI web version
🏦 Postgres migration
📡 Real-time WebSocket prices
🤖 Strategy backtesting module
## 📜 License

MIT License

## 👤 Author

Built as a fintech learning project focused on:

trading systems
portfolio mechanics
market data processing
