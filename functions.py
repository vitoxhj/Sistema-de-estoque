import json
from datetime import datetime

def open_stock():
    with open('stock.json', 'r', encoding='utf-8') as arquive:
        return json.load(arquive)
    
def open_movement():
    with open('movement.json', 'r', encoding='utf-8') as arquive:
        return json.load(arquive)

def save_stock(variavel):
    with open('stock.json', 'w', encoding='utf-8') as f:
        json.dump(variavel, f, indent=4, ensure_ascii=False)

def save_movement(variavel):
    with open('movement.json', 'w', encoding='utf-8') as f:
        json.dump(variavel, f, indent=4, ensure_ascii=False)

def date_now():
    date = datetime.now()
    date_formatad = date.strftime('%d/%m/%Y %H:%M:%S')
    return date_formatad

def get_view(product):
    print(f'Name: {product['name']}\nAmount: R${product['amount']}\nQuantity: {product['quantity']}')
    print(f'Category: {product['category']}\nValidity: {product['validity']}\nLot: {product['lot']}')
    print('-'*50)