from __future__ import annotations #per evitare gli import circolari
import src.logic.Player as Player
from abc import ABC, abstractmethod
symbols_utf = ["\u2717", "\u25ef"]
symbols_ascii = ["x", "o"]

class UI(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def stampa_tabellone(self, tabellone):
        '''stampa il terminale'''
        for i in range(0,8,3):
            print(f"| {tabellone[i]} | {tabellone[i+1]} | {tabellone[i+2]} |")
    def messaggio_benvenuto(self):
        '''stampa messaggio di benvenuto e attende input da utente'''
        print("benvenuto nella partita\npremi qualunque tasto per iniziare")
        input()     
    def print_giocatore(self, giocatore:str):
        '''stampa il giocatore di turno'''
        print(f"gioca il giocatore {giocatore}")
    def messaggio_vittoria(self, giocatore: Player.Player):
        '''stampa messaggio di vittoria per il giocatore in argomento'''
        print(f"HA VINTO {giocatore}")
    def messaggio_pareggio(self):
        '''stampa messaggio di pareggio'''
        print("La partita è patta")
def inserisci_casella() -> str:
        '''restitusce un input da terminale metodo statico per evitare di istanziare UI in player'''
        return input()
def stampa_errore(msg: str):
        '''stampa un messaggio di errore'''
        print(msg)

class UIUnicode(UI):
    def __init__(self):
        self.symbols = symbols_utf
class UIAscii(UI):
    def __init__(self):
        self.symbols = symbols_ascii