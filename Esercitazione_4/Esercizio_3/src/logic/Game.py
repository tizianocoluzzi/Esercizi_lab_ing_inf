from src.logic.Player import HumanPlayer, RandomPlayer, Player
from src.logic.UI import UIAscii, UIUnicode
from os import system
from time import sleep
'''manca di creare un main loop e la possibilita di scegliere ma non mi va'''
class Game:
    def __init__(self):
        pass
    def pieno(self, tabellone):
        '''resituisce true se il tabellone è pieno'''
        for i in tabellone:
            if (i == ' '):
                return False
        return True

    def vince(self, tabellone):
        '''restituisce il vincitore se c'è, altrimenti di 0'''
        for i in range(0,8,3):
            if(tabellone[i] != ' ' and tabellone[i] == tabellone[i+1] and tabellone[i] == tabellone[i+2]):
                return True
        for i in range(0,2,1):
            if(tabellone[i] != ' ' and tabellone[i] == tabellone[i+3] and tabellone[i] == tabellone[i+6]):
                return True
        if(tabellone[4] != ' ' and tabellone[0] == tabellone[4] and tabellone[0] == tabellone[8]):
            return True
        if(tabellone[4] != ' ' and tabellone[2] == tabellone[4] and tabellone[2] == tabellone[6]):
            return True
        return False

if __name__ == '__main__':
    ui = UIAscii()
    p1 = HumanPlayer(ui.symbols[0])
    p2 = HumanPlayer(ui.symbols[1])
    tabellone = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ui.messaggio_benvenuto()
    game = Game()
    g = p1
    i = 0
    v = False
    while(i < 9):
        system('cls')
        ui.print_giocatore(g.simbolo)
        ui.stampa_tabellone(tabellone)
        if(type(g) is RandomPlayer): #controlla e G è computer in modo da avere tempo di capire 
            sleep(1)
        g.mossa(tabellone)
        v = game.vince(tabellone) 
        if v:
            break
        g = p1 if (g is p2) else p2
        i += 1 #controllo sul numero di mosse
    system('cls')
    ui.stampa_tabellone(tabellone)
    if v:
        ui.messaggio_vittoria(g)
    else:
        ui.messaggio_pareggio()