from functions import *
from products import Product
from modifier import Modifier
from view import View
from database import database

def main():
    #database.stock()
    #database.movement()
    produto = Modifier(3)
    produto.removeProduct(20)

if __name__ == '__main__':
    main()