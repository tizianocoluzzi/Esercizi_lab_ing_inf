from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
template = Jinja2Templates(directory="./template") 
API_BASE_URL = "http://server-api:8000"

@app.get("/")
def welcome(request: Request):
    try:
        response = requests.get(f"{API_BASE_URL}/welcome")
        response.raise_for_status()
        r = response.json()
    except requests.RequestException as e:
        return template.TemplateResponse("error.html", {"request": request, "msg" :e}) 
    return template.TemplateResponse("index.html", {"request":request, "msg": r})

#in get per prendere il risultato
@app.get("/start")
def start_game(request: Request):
    try:
        response = requests.post(f"{API_BASE_URL}/startGame", json = {})
        response.raise_for_status()
        r = response.json()
    except requests.RequestException as e:
        print(f"errore: {e}")
    return template.TemplateResponse("game.html", {"request":request, "msg": r})

@app.get("/guess")
def guess(request: Request, num:str):
    try:
        print(num)
        response = requests.post(f"{API_BASE_URL}/guess/{num}", json = {})
        response.raise_for_status()
        r = response.json()
    except requests.RequestException as e:
        print(f"errore: {e}")
    return template.TemplateResponse("game.html", {"request":request, "msg": r})
