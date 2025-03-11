import random
from store_item.GenericItem import GenericItem
class NormalItem(GenericItem):
    def __init__(self, nome, prezzo):
        self.prezzo = prezzo
        self.nome = nome
    def tempo_spedizione(self):
        """ ritorna il tempo di spedizione tra 0 e 7 giorni"""
        return (int) (random.random()*10 % 7)
    def __str__(self):
        return f"{self.nome} : {self.prezzo} previsto in {self.tempo_spedizione()} giorni"