from datetime import datetime, timedelta
import sqlite3

line = '-'*50
class View:
    def __init__(self):
        pass

    def product(self):
        with sqlite3.connect("database/Stock_data.db") as stock:
            cursorStock = stock.cursor()
            cursorStock.execute("SELECT * FROM stocks")
            datas = cursorStock.fetchall()
        return datas

    def viewAll(self):
        datas = self.product()
        for data in datas:
            print(f"ID: {data[0]}\nName: {data[1]}\nQuantity: {data[2]}\nBuy: R${data[3]:.2f}\nSell: R${data[4]:.2f}\nCategory: {data[5]}\nValidity: {data[6]}\nLot: {data[7]}")
            print(line)

    def movementAll(self):
        with sqlite3.connect("database/Movement_data.db") as movement:
            cursor = movement.cursor()
            cursor.execute("SELECT * FROM movement")
            datas = cursor.fetchall()
        for data in datas:
            print(f"Type: {data[0]}\nName: {data[1]}\nBuy: R${data[2]:.2f}\nSell: R${data[3]:.2f}\nQuantity: {data[4]}\nDate: {data[5]}")
            print(line)
        

    def validity(self):
        stock = self.product()
        date = datetime.now().date()
        limit_expiring = date + timedelta(days=7)
        expired = []
        today = []
        expiring = []
        for product in stock:
            if not product[6]:
                continue
            try:
                validity = datetime.strptime(product[6], '%d/%m/%Y').date()
            except (TypeError, ValueError):
                continue
            if date > validity:
                expired.append(product)
            elif date == validity:
                today.append(product)
            elif date < validity <= limit_expiring:
                expiring.append(product)

        print('EXPIRED PRODUCTS'.center(50))
        print(line)
        for product in expired:
            print(product)

        print('PRODUCTS EXPIRING TODAY'.center(50))
        print(line)
        for product in today:
            print(product)
        print('PRODUCTS EXPIRING IN 7 DAYS'.center(50))
        print(line)
        for product in expiring:
            print(product)

        print(f'Expired: {len(expired)} products')
        print(f'Expired today: {len(today)} products')
        print(f'Expiring: {len(expiring)} products')

    def profit(self):
        with sqlite3.connect("database/Movement_data.db") as movement:
            cursorMovement = movement.cursor()
            cursorMovement.execute("SELECT * FROM movement")
            datas = cursorMovement.fetchall()
        gain = 0
        cost = 0
        loss = 0
        for info in datas:
            if info[0] == 'IN':
                money = info[2] * info[4]
                cost += money
            elif info[0] == 'OUT':
                money = info[3] * info[4]
                gain += money
            elif info[0] == 'DELETE':
                money = info[2] * info[4]
                loss += money
        profit1 = gain - cost - loss
        print(f'Gain: R${gain:.2f}')
        print(f'Cost: R${cost:.2f}')
        print(f'Loss: R${loss:.2f}')
        print(f'Profit: R${profit1:.2f}')

    def dateProfit(self, date):
        with sqlite3.connect("database/Movement_data.db") as movement:
            cursorMovement = movement.cursor()
            cursorMovement.execute("SELECT * FROM movement WHERE date >= (?)", (date,))
            datas = cursorMovement.fetchall()
        gain = 0
        cost = 0
        loss = 0
        for info in datas:
            if info[0] == 'IN':
                money = info[2] * info[4]
                cost += money
            elif info[0] == 'OUT':
                money = info[3] * info[4]
                gain += money
            elif info[0] == 'DELETE':
                money = info[2] * info[4]
                loss += money
        profit1 = gain - cost - loss
        print(f'Gain: R${gain:.2f}')
        print(f'Cost: R${cost:.2f}')
        print(f'Loss: R${loss:.2f}')
        print(f'Profit: R${profit1:.2f}')

    def allCategory(self):
        try:
            with sqlite3.connect("database/Stock_data.db") as stock:
                cursor = stock.cursor()
                cursor.execute("SELECT * FROM stocks")
                datas = cursor.fetchall()
            duplicate = []
            for data in datas:
                if data[5] in duplicate:
                    continue
                print(data[5])
                duplicate.append(data[5])
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def formated(self, data):
        print(f"ID: {data[0]}\nName: {data[1]}\nQuantity: {data[2]}\nBuy: R${data[3]:.2f}\nSell: R${data[4]:.2f}\nCategory: {data[5]}\nValidity: {data[6]}\nLot: {data[7]}")
        print(line)

    def search(self):
        choose = input("Choose a type for filter: ").strip().lower()
        if choose in ("quantity", "buy", "sell"):
            try:
                info = float(input(f"Choose a max {choose}: "))
            except ValueError:
                print("Type only numbers!")
                return
            with sqlite3.connect("database/Stock_data.db") as stock:
                cursor = stock.cursor()
                column = {"quantity": "quantity", "buy": "buy", "sell": "sell"}[choose]
                datas = cursor.execute(
                    f"SELECT * FROM stocks WHERE {column} <= (?)", (info,)
                ).fetchall()
            for data in datas:
                self.formated(data)
        elif choose == "category":
            info = input("Type a category: ").lower()
            with sqlite3.connect("database/Stock_data.db") as stock:
                datas = stock.execute("SELECT * FROM stocks WHERE category = (?)", (info,)).fetchall()
            for data in datas:
                self.formated(data)
        elif choose == "validity":
            info = input("Choose a max validity date: ")
            with sqlite3.connect("database/Stock_data.db") as stock:
                dates = stock.execute("SELECT * FROM stocks WHERE validity >= (?)", (info,)).fetchall()
            for date in dates:
                self.formated(date)
        elif choose == "lot":
            info = input("Type a lot: ").upper()
            with sqlite3.connect("database/Stock_data.db") as stock:
                datas = stock.execute("SELECT * FROM stocks WHERE lot = (?)", (info,)).fetchall()
            for data in datas:
                self.formated(data)
        elif choose == "type":
            info = input("Choose a type:").upper()
            with sqlite3.connect("database/Movement_data.db") as movement:
                dates = movement.execute("SELECT * FROM movement WHERE type = (?)", (info,)).fetchall()
            for data in dates:
                print(f"Type: {data[0]}\nName: {data[1]}\nBuy: R${data[2]:.2f}\nSell: R${data[3]:.2f}\nQuantity: {data[4]}\nDate: {data[5]}")
                print(line)
        else:
            print("Option unavailable")

    def removeValidity(self):
        date = datetime.now().date()
        limit_expiring = date + timedelta(days=7)
        with sqlite3.connect("database/Stock_data.db") as stock:
            cursor = stock.cursor()
            sell = cursor.execute("SELECT sell_price FROM stock").fetchall()
            cursor.execute("DELETE FROM stocks WHERE (?) > validity", (date, ))
            stock.commit()
            cursor.execute("UPDATE stocks SET sell_price = (?) WHERE (?) < validity < (?)", (0.30, date, limit_expiring))
            stock.commit()
            cursor.execute("UPDATE stocks SET sell_price = (?) WHERE (?) == validity", (0.65, date))
            stock.commit()
            print("Produtos atualizados!")