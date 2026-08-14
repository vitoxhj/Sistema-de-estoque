from functions import *
from movement import Movement
class Modifier:
    def __init__(self,id_product):
        self.id_product = id_product

    def removeProduct(self,quantity):
        stock = open_stock()
        quantity = int(quantity)
        for product in stock:
            if product['id'] == self.id_product:
                if quantity > product['quantity']:
                    print('Exceeded quantidy!')
                    return
                product['quantity'] -= quantity
                save_stock(stock)
                date = date_now()
                history = Movement('OUT',product['name'],quantity,date)
                history.save_movement()
                print(f'Product: {product['name']}')
                print(f'removed {quantity} products successfuly!')
                return
        print('Id not found!')

    def removeStock(self):
        stock = open_stock()
        for product in stock:
            if product['id'] == self.id_product:
                stock.remove(product)
                save_stock(stock)
                date = date_now()
                history = Movement('DELETE',product['name'],product['quantity'],date)
                history.save_movement()
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
                history = Movement('READ',product['name'],product['quantity'],date)
                history.create_movement()

