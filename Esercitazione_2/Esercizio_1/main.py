from customer.NormalCustomer import NormalCustomer
from customer.PromotionalCustomer import PromotionalCustomer
from store_item.NormalItem import NormalItem
from store_item.ForeignItem import ForeignItem
from store.Store import Store
from ui.Ui import login
from ui.Ui import lista_item
import time
def init_store():
    store = Store(200)
    i1 = NormalItem("i1", 100);
    i2 = NormalItem("i2", 20)
    i3 = ForeignItem("i3", 40)
    if store.aggiungi_item(i1) == -1:
        print("aggiunta andata male")

    if store.aggiungi_item(i2) == -1:
        print("aggiunta andata male")
    if store.aggiungi_item(i2) == -1:
        print("aggiunta andata male")

    if store.aggiungi_item(i3) == -1:
        print("aggiunta andata male")
    return store
if __name__ == '__main__':
    cred = login()
    nome = cred[0]
    budget = cred[1]
    if(cred[2] == 1):
        user = PromotionalCustomer(nome, budget)
    else:
        user = NormalCustomer(nome, budget)
    store = init_store()
    while(True):
        a = lista_item(store, user)
        if(a == "quit"):
            print("grazie per l'acquisto!!")
            break;
        item = store.cerca_item(a)
        print(f"vuoi acquistare {item}?")
        ret = user.acquisto(item)
        if ret == -1:
            print("acquisto non andato a buon fine");
        else:
            ret = store.vendi_item(item)
            if(ret == -1):
                print("purtroppo non ci sono abbastanza item")
                user.accredito(item.prezzo) #accredito l'importo non andato a buo fine
            else:
                print("acquisto andato a buon fine")
        time.sleep(2)
