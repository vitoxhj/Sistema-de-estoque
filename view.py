from functions import *
from datetime import datetime, timedelta

line = '-'*50
class View:
    def __init__(self):
        pass

    def viewAll(self):
        stock = open_stock()
        print('ALL PRODUCTS'.center(50))
        print(line)
        for products in stock:
            get_view(products)
        print(f'Quantity of products: {len(stock)}')

    def validity(self):
        stock = open_stock()
        date = datetime.now().date()
        limit_expiring = date + timedelta(days=7)
        expired = []
        today = []
        expiring = []
        for product in stock:
            if not product['validity']:
                continue
            validity = datetime.strptime(product['validity'], '%d/%m/%Y').date()
            if date > validity:
                expired.append(product)
            elif date == validity:
                today.append(product)
            elif date < validity <= limit_expiring:
                expiring.append(product)

        print('EXPIRED PRODUCTS'.center(50))
        print(line)
        for product in expired:
            get_view(product)

        print('PRODUCTS EXPIRING TODAY'.center(50))
        print(line)
        for product in today:
            get_view(product)
        print('PRODUCTS EXPIRING IN 7 DAYS'.center(50))
        print(line)
        for product in expiring:
            get_view(product)

        print(f'Expired: {len(expired)} products')
        print(f'Expired today: {len(today)} products')
        print(f'Expiring: {len(expiring)} products')

    def profit(self):
        movement = open_movement()
        gain = 0
        cost = 0
        loss = 0
        for info in movement:
            if info['type'] == 'IN':
                money = info['buy_price'] * info['quantity']
                cost += money
            elif info['type'] == 'OUT':
                money = info['sell_price'] * info['quantity']
                gain += money
            elif info['type'] == 'DELETE':
                money = info['buy_price'] * info['quantity']
                loss += money
        profit1 = gain - cost - loss
        print(f'Gain: ${gain:.2f}')
        print(f'Cost: ${cost:.2f}')
        print(f'Loss: ${loss:.2f}')
        print(f'Profit: ${profit1:.2f}')
