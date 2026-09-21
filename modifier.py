from functions import *
from movement import Movement
import sqlite3
from datetime import datetime
class Modifier:
    def __init__(self,id_product):
        self.id_product = id_product

    def productId(self):
        stock = sqlite3.connect("database/Stock_data.db")
        cursorStock = stock.cursor()
        cursorStock.execute("SELECT name, quantity, buy_price, sell_price FROM stocks WHERE id = (?)", (self.id_product,))
        datas = cursorStock.fetchone()
        if datas is None:
            print("Produto não encontrado")
            stock.close()
            return

        stock.close()
        return datas

    def removeProduct(self,quantity):
        try:
            name, quant, buy, sell = self.productId()
            stock = sqlite3.connect("database/Stock_data.db")
            cursorStock = stock.cursor()

            if quantity > quant or quantity <= 0:
                print("Error na quantidade escolhida")
                stock.close()
                return
            total = quant - quantity
            cursorStock.execute("UPDATE stocks SET quantity = (?) WHERE id = (?)", (total, self.id_product))
            stock.commit()
            stock.close()
            time = datetime.now()
            movement = sqlite3.connect("database/Movement_data.db")
            cursorMovement = movement.cursor()
            cursorMovement.execute("""INSERT INTO movement (type, name, buy_price, sell_price, quantity, date)
                                        VALUES (?, ?, ?, ?, ?, ?)""", ("OUT", name, buy, sell, quantity, time))
            movement.commit()
            movement.close()
            print(f"Produto alterado: {name}\nQuantidade atual: {total}")
            print("Produto removido!")
        except sqlite3.Error as error:
            print(f"Erro ao remover produto: {error}")

    def removeStock(self):
        try:
            name, quant, buy, sell = self.productId()
            stock = sqlite3.connect("database/Stock_data.db")
            cursorStock = stock.cursor()
            cursorStock.execute("DELETE FROM stocks WHERE id = (?)", (self.id_product,))
            stock.commit()
            stock.close()
            time = datetime.now()
            movement = sqlite3.connect("database/Movement_data.db")
            cursorMovement = movement.cursor()
            cursorMovement.execute("""INSERT INTO movement (type, name, buy_price, sell_price, quantity, date)
                                        VALUES (?, ?, ?, ?, ?, ?)""", ("DELETE", name, buy, sell, quant, time))
            movement.commit()
            movement.close()
            print(f"Estoque deletado: {name}")
            print("Estoque deletado com sucesso!")
        except sqlite3.Error as error:
            print(f"Erro ao deletar estoque: {error}")

    def viewProduct(self):
        try:
            name, quant, buy, sell = self.productId()
            stock = sqlite3.connect("database/Stock_data.db")
            cursorStock = stock.cursor()
            cursorStock.execute("SELECT * FROM stocks WHERE id = (?)", (self.id_product,))
            print(cursorStock.fetchall())
            stock.close()
            time = datetime.now()
            movement = sqlite3.connect("database/Movement_data.db")
            cursorMovement = movement.cursor()
            cursorMovement.execute("""INSERT INTO movement (type, name, buy_price, sell_price, quantity, date)
                                        VALUES (?, ?, ?, ?, ?, ?)""", ("READ", name, buy, sell, quant, time))
            movement.commit()
            movement.close()

        except sqlite3.Error as error:
            print(f"Erro ao visualizar produto: {error}")
