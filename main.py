from functions import *
from products import Product
from modifier import Modifier
from view import View
from database import database

def main():
    #database.stock()
    #database.movement()
    #produto = Product("Abrobinha", 100, 7, 10, "Legumes", "15/12/2026", "JHW198")
    #produto.create()

    produto = View()
    produto.profit()
    produto.dateProfit("08/17/2026")

if __name__ == '__main__':
    main()