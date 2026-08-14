from functions import *
from movement import Movement

class Product:
        def __init__(self,name,quantity,amount,category,validity,lot):
            self.name = name
            self.quantity = int(quantity)
            self.amount = float(amount)
            self.category = category.lower()
            self.validity = validity
            self.lot = lot

        def create(self):
            stock = open_stock()
            date = date_now()
            new_id = 1
            while any(info['id'] == new_id for info in stock):
                new_id += 1

            info = {
                'id': new_id,
                'name': self.name,
                'quantity': self.quantity,
                'amount': self.amount,
                'category': self.category,
                'validity': self.validity,
                'lot': self.lot
            }
            stock.append(info)
            save_stock(stock)
            history = Movement('IN',self.name,self.quantity,date)
            history.save_movement()
            print('Product created successfuly!')
    


    