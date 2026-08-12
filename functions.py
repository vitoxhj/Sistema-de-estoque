import os
import json
import re
from datetime import datetime

#Create a json
def stock_json(variavel,dados):
    if not os.path.exists(variavel):
        with open(variavel, 'w', encoding='utf-8') as f:
            json.dump(dados, f , indent=4, ensure_ascii=False)
    else:
        return

def movement_json(variavel,dados):
    if not os.path.exists(variavel):
        with open(variavel, 'w', encoding='utf-8') as f:
            json.dump(dados, f , indent=4, ensure_ascii=False)
    else:
        return
    
#Open a json 
def open_stock():
    with open('stock.json', 'r', encoding='utf-8') as arquive:
	    return json.load(arquive)

def open_movement():
    with open('movement.json', 'r', encoding='utf-8') as arquive:
	    return json.load(arquive)

#Save a json 
def save_stock(variavel):
    with open('stock.json', 'w', encoding='utf-8') as f:
        json.dump(variavel, f, indent=4, ensure_ascii=False)

def save_movement(variavel):
    with open('movement.json', 'w', encoding='utf-8') as f:
        json.dump(variavel, f, indent=4, ensure_ascii=False)

line = '-'*50

def choose_formatad(min,max):
     while True:
        try:
            option = int(input('->'))
            print(line)
        except ValueError:
            print(line)
            print('Type only numbers!')
            print(line)
            continue
        if option < min or option > max:
            print('Option unavailabe!')
            print(line)
            continue
        return option
     
def interface():
     stock = open_stock()
     print(line)
     print('Stock Systeam'.center(50))
     print(line)
     print('1 - Create a Product')
     print('2 - Remove a Product')
     print('3 - Remove a Stock')
     print('4 - Edit Product')
     print('5 - List Stock')
     print('6 - Look up Product')
     print('7 - Transaction history')
     print('8 - Export for .CSV')
     print('9 - Exit')
     print(line)
     print(f'Total of Products: {len(stock)}')
     print(line)
     min = 1
     max = 9
     option = choose_formatad(min,max)
     return option

def get_amount():
    while True:
        amount = input('Amount: ').strip()
        print(line)

        # Remove R$ and spaces
        amount = amount.replace('R$', '').replace('r$', '').strip()

        # Verify
        if not amount:
            print('Amount cannot be empty!')
            print(line)
            continue

        # Format:
        pattern = r'^\d{1,3}(?:\.\d{3})*(?:,\d{1,2})?$|^\d+(?:,\d{1,2})?$'

        if not re.fullmatch(pattern, amount):
            print('Invalid amount!')
            print()
            print('Examples: 10 | 10,50 | 1.234,56')
            print(line)
            continue

        # Remove milhar
        amount = amount.replace('.', '')

        # Troca vírgula decimal por ponto
        amount = amount.replace(',', '.')

        try:
            amount = float(amount)
            return amount

        except ValueError:
            print('Invalid amount!')
            print(line)

def create_product():
    stock = open_stock()
    movement = open_movement()
    while True:
        name = input('Name: ')
        print(line)
        amount = get_amount()
        print(line)
        try:
            quantity = int(input('Quantity:'))
            print(line)
        except ValueError:
            print('Type only numbers!')
            print(line)
            continue

        new_id = 1
        while any(product['id'] == new_id for product in stock):
            new_id += 1

        date = datetime.now()
        date_formatad = date.strftime('%d/%m/%Y %H:%M:%S')
        info_stock = {
            'id': new_id,
            'name': name,
            'amount': amount,
            'quantity': quantity
        }
        stock.append(info_stock)
        save_stock(stock)

        info_movement = {
            'Type': 'Post',
            'id': new_id,
            'name': name,
            'entry_quantity': quantity,
            'date': date_formatad
        }
        movement.append(info_movement)
        save_movement(movement)
        print('Product created successfuly!')
        return