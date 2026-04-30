import sqlite3

DB = "portfolio.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # cash account
    c.execute("""
    CREATE TABLE IF NOT EXISTS account (
        id INTEGER PRIMARY KEY,
        cash REAL NOT NULL DEFAULT 10000
    )
    """)

    # positions
    c.execute("""
    CREATE TABLE IF NOT EXISTS positions (
        symbol TEXT PRIMARY KEY,
        quantity REAL NOT NULL,
        avg_price REAL NOT NULL
    )
    """)

    # trades history
    c.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        side TEXT NOT NULL,
        quantity REAL NOT NULL,
        price REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # init cash if missing
    c.execute("SELECT cash FROM account WHERE id = 1")
    if c.fetchone() is None:
        c.execute("INSERT INTO account (id, cash) VALUES (1, 10000)")

    conn.commit()
    conn.close()



# cash


def get_cash():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT cash FROM account WHERE id = 1")
    cash = c.fetchone()[0]

    conn.close()
    return cash


def update_cash(new_cash: float):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("UPDATE account SET cash = ? WHERE id = 1", (new_cash,))

    conn.commit()
    conn.close()


# positions

def load_positions():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT symbol, quantity, avg_price FROM positions")
    rows = c.fetchall()

    conn.close()
    return rows


def upsert_position(symbol: str, quantity: float, avg_price: float):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO positions (symbol, quantity, avg_price)
    VALUES (?, ?, ?)
    ON CONFLICT(symbol)
    DO UPDATE SET
        quantity = excluded.quantity,
        avg_price = excluded.avg_price
    """, (symbol, quantity, avg_price))

    conn.commit()
    conn.close()


# trades

def log_trade(symbol: str, side: str, qty: float, price: float):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO trades (symbol, side, quantity, price)
    VALUES (?, ?, ?, ?)
    """, (symbol, side, qty, price))

    conn.commit()
    conn.close()
