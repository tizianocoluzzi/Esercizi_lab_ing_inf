from random import randint

file:str = "results.tsv" 

#aggiustare la logica

class Game:
    def __init__(self)->None:
        '''costruttore'''
        try:

            with open(file, "r") as f:
                l = f.readline()
                if(l):
                    self.number = int(l)
                else:
                    self.new_game()
        except:
            self.new_game()
    def res(self, number)->str:
        '''resituisce una stringa con le indicazioni, lancia un'eccezione se il gioco è finito'''
        if(self.guessed): 
            return "il gioco è finito, il numero è stato indovinato in precedenza"
        try:
            n = int(open(file,"r").readline())
        except:
            return "errore, partita non inizializzata"
        
        if(number > n):
            return "il numero scelto è maggiore, tenta piu in basso"
        elif(number < n):
            return "il numero scelto è minore, tenta piu in alto"
        else:
            self.guessed = True
            return "complimenti hai indovinato"
    
    def new_game(self):
        '''inizializza un nuovo gioco nel file file'''
        self.number = randint(0,100)
        self.guessed = False
        with open(file, "w") as f:
            f.write(str(self.number))