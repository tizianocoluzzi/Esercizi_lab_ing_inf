from __future__ import annotations #per evitare gli import circolari
from abc import ABC, abstractmethod
from typing import List
import random
import src.logic.UI as UI
class Player(ABC):
    @abstractmethod
    def __init__(self, simbolo):
        self.simbolo = simbolo
    def mossa(self, tabellone):
        pass
    @abstractmethod
    def __str__(self):
        pass

class HumanPlayer(Player):
    def __init__(self, simbolo):
        super().__init__(simbolo)
        pass
    def mossa(self, tabellone:List[str], casella:int):
        '''chiede input a utente e fa sideeffect con tabellone'''
        try:
            #x = int(UI.inserisci_casella()) - 1
            x = int(casella)
            if(tabellone[x] != " "):
                raise Exception("casella gia inserita")
            tabellone[x] = self.simbolo
        except ValueError:
            raise Exception("casella inserita non valida")
    
    def __str__(self):
        return f"giocatore umano con simbolo {self.simbolo}"
class RandomPlayer(Player):
    def __init__(self, simbolo):
        super().__init__(simbolo)
        pass

    def mossa(self, tabellone):
        '''fa side effect su tabellone'''

        x = random.randint(0,8)
        while(tabellone[x] != ' '):
            x = random.randint(0,8)
        tabellone[x] = self.simbolo
    def __str__(self):
        return f"giocatore cpu con simbolo {self.simbolo}"