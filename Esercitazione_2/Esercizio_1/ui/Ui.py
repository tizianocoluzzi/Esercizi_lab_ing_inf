from store.Store import Store
import os
def login():
    print("Benvenuto nel nostr e-commerce:\nIdentificati")
    nome = input()
    print(f"Ottimo {nome}, quanto budget hai?")
    budget = input()
    print("un ultima domanda, sei in possesso di un codice promozionale?[y/n]")
    res = input()
    if(res == 'y'):
        return (nome, int(budget), 1)
    return (nome, int(budget), 0)

def lista_item(store:Store, utente):
    os.system('cls')
    print(f"{utente.nome} {utente.b}")
    print("scegli cosa acquistare: ")
    print(store.mostra_item())
    acquisto = input()
    return acquisto
