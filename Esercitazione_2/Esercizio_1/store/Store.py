from store_inventory.StoreInventory import StoreInventory
from store_item.GenericItem import GenericItem
from customer.GenericCustomer import GenericCustomer
class Store:
    def __init__(self, denaro:int)->None:
        self.inventory = StoreInventory()
        self.denaro = denaro
        self.diz_nomi = {}
    def aggiungi_item(self, item:GenericItem)->bool:
        """aggiungi item vuol dire che il negozio acquista l'oggetto alla meta del prezzo di vendita
        return False se impossibile l'acquisto"""
        prezzo = item.prezzo * 0.5
        if(self.denaro < prezzo):
            return False
        # NON POSSONO ESISTE DUE ITEM CON LO STESSO NOME E PREZZI DIVERSI
        if(item.nome in self.diz_nomi):
            if(item not in self.inventory.inventario.keys()):
                return False
        else:
            self.diz_nomi[item.nome] = item ##se non è nel dizionario dei nomi allora lo aggiungo 
        self.inventory.aggiungiItem(item)
        self.denaro -= prezzo
        return True
    def vendi_item(self, item:GenericItem, user:GenericCustomer)->bool:
        """vende l'item item all'utente user, ritorna False se non abbastanza item o se l'utente non puo comprare"""
        if(not self.inventory.rimuoviItem(item) or not user.acquisto(item)): 
            return False # problemino perche abbiamo che le funzioni vengono eseguite quindi se non ci sono abbastanza item comunque il saldo dell'utente viene scalato
        self.denaro += item.prezzo
        return 0
    def mostra_item(self)->None:
        str = ""
        for i in self.inventory.inventario.keys():
            if(self.inventory.inventario[i] > 0):
                str += f"{i} q.ta {self.inventory.inventario[i]}\n"
        return str
    def cerca_item(self, nome):
        return self.diz_nomi[nome]