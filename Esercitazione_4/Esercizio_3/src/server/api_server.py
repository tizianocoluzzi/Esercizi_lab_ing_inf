from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.logic.Player import Player, HumanPlayer, RandomPlayer
from src.logic.Game import Game
app = FastAPI()

players: List[Player] = []
tabellone: List[str] = [" " for _ in range(0,9)]
game: Game = Game()
players.append(HumanPlayer('x'))
players.append(HumanPlayer('o'))



class Response(BaseModel):
    res: str

class TabelloneResponse(BaseModel):
    res:str
    tabellone: List[str]
    player: str

@app.get("/welcome")
def welcome()->Response:
    '''ritorna messaggio di benvenuto'''
    return Response(res = "welcome")

@app.post("/startGame")
def start_game()->TabelloneResponse:
    '''ritorna tabellone inizializzato'''
    tabellone = [" " for _ in range(0,9)]
    return TabelloneResponse(res = "game started", tabellone = tabellone, player = players[0].simbolo)

@app.post("/game/{player}/{casella}")
def move(player:str, casella:str)->TabelloneResponse:
    '''giocatore player esegue la mossa casella''' 
    if(players[0].simbolo == player):
        p = players[1].simbolo
        players[0].mossa(tabellone, casella)
    else:
        p = players[0].simbolo
        players[1].mossa(tabellone, casella)
    if(game.vince(tabellone)):
        return TabelloneResponse(res = "vittoria del giocatore corrente", tabellone = tabellone, player = player)
    elif(game.pieno(tabellone)):
        return TabelloneResponse(res = "pareggio", tabellone = tabellone, player=p)
    return TabelloneResponse(res = "mossa effettuata", tabellone = tabellone, player = p)