from functions import *
from datetime import datetime, timedelta
import sqlite3

line = '-'*50
class View:
    def __init__(self):
        pass

    def product(self):
        stock = sqlite3.connect("database/Stock_data.db")
        cursorStock = stock.cursor()
        cursorStock.execute("SELECT * FROM stocks")
        datas = cursorStock.fetchall()
        stock.close()
        return datas

    def viewAll(self):
        datas = self.product()
        for data in datas:
            print()
            for info in data:
                print(f"{info}, ",end="")

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
            validity = datetime.strptime(product[6], '%d/%m/%Y').date()
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
        movement = sqlite3.connect("database/Movement_data.db")
        cursorMovement = movement.cursor()
        cursorMovement.execute("SELECT * FROM movement")
        datas = cursorMovement.fetchall()
        #print(datas)
        movement.close()
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
        print(f'Gain: ${gain:.2f}')
        print(f'Cost: ${cost:.2f}')
        print(f'Loss: ${loss:.2f}')
        print(f'Profit: ${profit1:.2f}')

    def dateProfit(self, date):
        movement = sqlite3.connect("database/Movement_data.db")
        cursorMovement = movement.cursor()
        cursorMovement.execute("SELECT * FROM movement WHERE date <= DATE(?)", (date,))
        datas = cursorMovement.fetchall()
        #print(datas)
        movement.close()
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
        print(f'Gain: ${gain:.2f}')
        print(f'Cost: ${cost:.2f}')
        print(f'Loss: ${loss:.2f}')
        print(f'Profit: ${profit1:.2f}')
