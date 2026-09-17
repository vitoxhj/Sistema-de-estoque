import sqlite3

def stock():
    conection = sqlite3.connect("Stock_data.db")
    cursor = conection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS stocks (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    buy_price FLOAT NOT NULL,
                    sell_price FLOAT NOT NULL,
                    category TEXT NOT NULL,
                    validity DATE NOT NULL,
                    lot TEXT NOT NULL)""")

    conection.commit()

def movement():
    conection = sqlite3.connect("Movement_data.db")
    cursor = conection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS movement (
                    type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    buy_price FLOAT NOT NULL,
                    sell_price FLOAT NOT NULL,
                    quantity INTEGER NOT NULL,
                    date DATETIME NOT NULL)""")

    conection.commit()