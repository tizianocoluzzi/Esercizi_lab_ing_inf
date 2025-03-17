from __future__ import annotations #per evitare gli import circolari
from abc import ABC, abstractmethod
import random
import UI
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
    def mossa(self, tabellone):
        '''chiede input a utente e fa sideeffect con tabellone'''
        print("inserisci casella scelta[1-9]:")
        try:
            x = int(UI.inserisci_casella()) - 1
            while(tabellone[x] != ' '):
                UI.stampa_errore("la casella scelta è gia popolata\ninserisci casella[1-9]")
                x = int(UI.inserisci_casella()) -1
            tabellone[x] = self.simbolo
        except:
            UI.stampa_errore("inserita casella non valida")
            self.mossa(tabellone)
    
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