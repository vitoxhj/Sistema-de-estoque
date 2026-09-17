from functions import *
from movement import Movement
import sqlite3
from datetime import datetime
class Modifier:
    def __init__(self,id_product):
        self.id_product = id_product

    def removeProduct(self,quantity):
        try:
            stock = sqlite3.connect("database/Stock_data.db")
            cursorStock = stock.cursor()
            cursorStock.execute("SELECT name, quantity, buy_price, sell_price FROM stocks WHERE id = (?)", self.id_product)
            datas = cursorStock.fetchone()
            name, quant, buy, sell = datas
            if quantity > quant or quantity <= 0:
                print("Error na quantidade escolhida")
                return
            total = quant - quantity
            cursorStock.execute("UPDATE stocks SET quantity = (?) WHERE id = (?)", total, self.id_product)
            print(f"Produto alterado: {name}\nQuantidade atual: {total}")
            stock.commit()
            stock.close()
            type = "OUT"
            time = datetime.now()
            movement = sqlite3.connect("database/Movement_data.db")
            cursorMovement = movement.cursor()
            cursorMovement.execute("""INSERT INTO movement (type, name, buy_price, sell_price, quantity, date)
                                        VALUES (?, ?, ?, ?, ?, ?)""", type, name, buy, sell, quant, time)
            print("Produto removido!")
        except sqlite3.Error as error:
            print(f"Erro ao remover produto: {error}")

    def removeStock(self):
        stock = open_stock()
        for product in stock:
            if product['id'] == self.id_product:
                stock.remove(product)
                save_stock(stock)
                date = date_now()
                history = Movement('DELETE',product['name'],product['buy_price'],product['sell_price'],product['quantity'],date)
                history.create_movement()
                print(f'Stock: {product['name']}')
                print('Stock removed successfuly!')
                return
        print('Id not found!')
        return
    
    def viewProduct(self):
        stock = open_stock()
        for product in stock:
            if product['id'] == self.id_product:
                get_view(product)
                date = date_now()
                history = Movement('READ',product['name'],product['buy_price'],product['sell_price'],product['quantity'],date)
                history.create_movement()

