import random
from store_item.GenericItem import GenericItem
class ForeignItem(GenericItem):
    def __init__(self, nome, prezzo):
        self.prezzo = prezzo
        self.nome = nome
    def tempo_spedizione(self):
        """ ritorna il tempo di spedizione tra 5 e 20 giorni"""
        return (int)( 5 + random.random()*10 % 15)
    def __str__(self):
        return f"{self.nome} : {self.prezzo} previsto in {self.tempo_spedizione()} giorni STRANIERO"