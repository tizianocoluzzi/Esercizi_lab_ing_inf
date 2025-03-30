from fastapi import Request, FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
import requests

API_BASE_URL = "http://127.0.0.1:8000"

templates = Jinja2Templates(directory="./templates")
player: str = 'x'

app = FastAPI()

@app.get("/")
def welcome(request:Request):
    response = requests.get(f"{API_BASE_URL}/welcome")
    response.raise_for_status()
    r = response.json()
    return templates.TemplateResponse("index.html", {'request': request, 'msg': r})

@app.get("/start")
def newGame(request: Request):
    player = 'x'
    response = requests.post(f"{API_BASE_URL}/startGame", json = {})
    response.raise_for_status()
    r = response.json()
    return templates.TemplateResponse("game.html", {'request': request, 'msg': r})

@app.get("/game")
def move(request: Request, casella: str, player:str):
    response = requests.post(f"{API_BASE_URL}/game/{player}/{casella}", json={})
    response.raise_for_status()
    r = response.json()
    if(r['res'] == "vittoria del giocatore corrente"):
        return templates.TemplateResponse("vittoria.html", {'request': request, 'msg':r})
    if(r['res'] == "pareggio"):
        return templates.TemplateResponse("pareggio.html", {'request': request, 'msg':r})
    return templates.TemplateResponse("game.html", {'request': request, 'msg': r})