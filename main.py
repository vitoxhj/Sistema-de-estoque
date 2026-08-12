from functions import *

def main():
    while True:
        stock_json('stock.json', [])
        movement_json('movement.json', [])
        option = interface()
        if option == 1:
            create_product()

if __name__ == '__main__':
    main()