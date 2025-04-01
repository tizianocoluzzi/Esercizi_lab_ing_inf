from Player import *
import random
import datetime
import time
def game(player: Player):
    while(True):
            guess = player.guess()
            print(f"giocatore prova con {guess}")
            mmu = guess-num
            print(f"la distanza è {mmu}")
            player.check_guess(mmu)
            print(f"player mmu {player.mmu}")
            if(mmu == 0):
                print(f"vinto gioco in {player.tentativi}")
                with open("fastplayer.tsv", "a") as file:
                    file.write(f"player:{player.nome} vinto in {player.tentativi} in data {datetime.datetime.now()}\n")
                break
            #time.sleep(0.5)

if __name__ == '__main__':
    MAX = 400000000 
    player = FastPlayer("fastpc",MAX)
    i = 0
    while(i < 100):
        i+=1
        player.reset(MAX) ##riporto i valori originali
        num = random.randint(0,MAX)
        #x = input("inziare il gioco?[y,n]")
        #if(x == 'y'):
            #player.tentativi = 0
        game(player)
        #else:
        #    break
        


