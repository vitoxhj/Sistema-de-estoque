from functions import save_movement,open_movement

class Movement:
    def __init__(self,type,name,buy,sell,quantity,date):
        self.type = type
        self.name = name
        self.quantity = int(quantity)
        self.date = date
        self.buy = float(buy)
        self.sell = float(sell)

    def create_movement(self):
        dados = open_movement()
        info = {
            'type': self.type,
            'name': self.name,
            'buy_price': self.buy,
            'sell_price': self.sell,
            'quantity': self.quantity,
            'date': self.date
        }
        dados.append(info)
        save_movement(dados)