
from products import Product
from modifier import Modifier
from view import View
from database import database

def main():
    #database.stock()
    #database.movement()
    #produto = Product("Guarana", 100, 7, 100, "Fruta", "20/09/2026", "JHW198")
    #produto.create()
    #produto = Product("Guarana", 100, 7, 100, "Fruta", "24/09/2026", "JHW198")
    #produto.create()
    #produto = Product("Guarana", 100, 7, 100, "Fruta", "28/09/2026", "JHW198")
    #produto.create()

    produto = View()
    produto.removeValidity()

if __name__ == '__main__':
    main()