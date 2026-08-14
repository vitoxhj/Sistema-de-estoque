from functions import *

class View:
    def __init__(self):
        pass

    def viewAll(self):
        stock = open_stock()
        for products in stock:
            print(f'Id: {products['id']}')
            get_view(products)
