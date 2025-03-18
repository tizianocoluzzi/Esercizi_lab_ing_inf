import random
from store_item.GenericItem import GenericItem
class ForeignItem(GenericItem):
    def __init__(self, nome, prezzo)->None:
        self.prezzo = prezzo
        self.nome = nome
    def tempo_spedizione(self)->int:
        """ ritorna il tempo di spedizione tra 5 e 20 giorni"""
        return (int)( 5 + random.random()*10 % 15)
    def __str__(self)->str:
        return f"{self.nome} : {self.prezzo} previsto in {self.tempo_spedizione()} giorni STRANIERO"