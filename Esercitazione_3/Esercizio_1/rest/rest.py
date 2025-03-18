from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  #non l'ho usata perche boh
from typing import Dict
# importa la logica
from logic.customer.GenericCustomer import GenericCustomer
from logic.customer.NormalCustomer import NormalCustomer
from logic.customer.PromotionalCustomer import PromotionalCustomer
from logic.store.Store import Store
from logic.store_item.GenericItem import GenericItem
from logic.store_item.NormalItem import NormalItem
from logic.store_item.ForeignItem import ForeignItem
app = FastAPI()

'''
creazione dello store perche non ho la minima integrazione con un database'
probabilmente bisognerebbe avere la logica che aggiorna un database ogni volta che si fa un'operazione
'''
store = Store(10000)
i1 = NormalItem("caccola", 100)
i2 = ForeignItem("LUCA", 103)
i3 = NormalItem("grasso_che_cola", 1000)

store.aggiungi_item(i1)
store.aggiungi_item(i1)
store.aggiungi_item(i1)
store.aggiungi_item(i2)
store.aggiungi_item(i3)
store.aggiungi_item(i3)

users: Dict[str, GenericCustomer] = {}
users["Franco"] = PromotionalCustomer("Franco", 100)
users["Maria"] = NormalCustomer("Maria", 100)

class User(BaseModel):
    user_name: str
#classe di risposta per richiesta di lista item di utente
class UserItemsResponse(BaseModel):
    user_name: str
    resp: str
# classe di risposta per get inventario, sarebbe da fare anche per item
class InventoryResponse(BaseModel):
    inventory: str
class ItemResponse(BaseModel):
    info: str

class PurchaseResponse(BaseModel):
    user: User
    item: ItemResponse

@app.get("/get_inventory/")
def get_inventory()->InventoryResponse:
    return InventoryResponse(inventory = f"{store.inventory}")

@app.get("/get_items/{user_name}")
def get_user_items(user_name: str)->UserItemsResponse:
    if(user_name not in users.keys()):
        raise HTTPException( status_code= 404 , detail = "users Not Found")
    return UserItemsResponse(resp = f"{users[user_name].items}", user_name = user_name)

@app.get("/get_item_information/{item_name}")
def get_item_information(item_name: str)->ItemResponse:
    if(item_name not in store.diz_nomi.keys()):
        raise HTTPException(status_code= 404, detail="item not found")
    return ItemResponse(info= f"{store.diz_nomi[item_name]}")

@app.get("/get_balance/{user_name}")
def get_balance(user_name:str)->int:
    if(user_name not in users.keys()):
        raise HTTPException( status_code= 404 , detail = "users Not Found")
    return users[user_name].b

@app.post("/purchase/{user_name}/{item_name}")
def purchase(user_name: str, item_name: str)->PurchaseResponse:
    if(user_name not in users.keys()):
        raise HTTPException(status_code=404, detail = "user not found")
    if(item_name not in store.diz_nomi.keys()):
        raise HTTPException(status_code=404, detail= "item not found")
    i = store.diz_nomi[item_name]
    u =  users[user_name]
    res = store.vendi_item(i,u)
    
    return PurchaseResponse(user = User(user_name = user_name, resp = f"{u}"), item=ItemResponse(info = f"{i}"))