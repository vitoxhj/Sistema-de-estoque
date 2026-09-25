from datetime import datetime
import sqlite3

class Product:
        def __init__(self,name,quantity,buy,sell,category,validity,lot):
            self.name = name
            self.quantity = int(quantity)
            self.buy = float(buy)
            self.sell = float(sell)
            self.category = category.lower()
            self.validity = validity
            self.lot = lot

        def create(self):
            try:
                date = datetime.now()
                type = "IN"
                conectionStock = sqlite3.connect("database/Stock_data.db")
                cursorStock = conectionStock.cursor()

                cursorStock.execute("""INSERT INTO stocks
                                        (name,quantity,buy_price,sell_price,category,validity,lot) VALUES
                                        (?, ?, ?, ?, ?, ?, ?)""",
                                        (self.name, self.quantity, self.buy, self.sell, self.category, self.validity, self.lot))

                conectionStock.commit()
                conectionStock.close()

                conectionMovement = sqlite3.connect("database/Movement_data.db")
                cursorMovement = conectionMovement.cursor()

                cursorMovement.execute("""INSERT INTO movement
                                        (type,name,buy_price,sell_price,quantity,date) VALUES
                                        (?, ?, ?, ?, ?, ?)""",
                                        (type, self.name, self.buy, self.sell, self.quantity, date))

                conectionMovement.commit()
                conectionMovement.close()
                print('Product created successfuly!')
            except sqlite3.Error as erro:
                print(f"Erro in create product: {erro}")

    


    