from functions import save_movement,open_movement

class Movement:
    def __init__(self,type,name,quantity,date):
        self.type = type
        self.name = name
        self.quantidy = int(quantity)
        self.date = date

    def create_movement(self):
        dados = open_movement()
        info = {
            'type': self.type,
            'name': self.name,
            'quantidy': self.quantidy,
            'date': self.date
        }
        dados.append(info)
        save_movement(dados)