from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
from src.Game import Game
from typing import List


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


class Result(BaseModel):
    res: str

game = Game()


@app.get("/welcome")
def welcome()-> Result:
    '''ritorna messaggio di benvenuto'''
    return Result(res = "benvenuto nel gioco indovina un numero")

@app.post("/startGame")
def start()->Result:
    '''inizializza un nuovo gioco'''
    game.new_game()
    assert(game)
    return Result(res = "game started")

@app.post("/guess/{num}")
def guess(num:int)->Result:
    '''restituisce se il risultato è minore o maggiore'''
    assert(game)
    r = game.res(num)
    return Result(res = r)
