from store_inventory.StoreInventory import StoreInventory
class Store:
    def __init__(self, denaro):
        self.inventory = StoreInventory()
        self.denaro = denaro
        self.diz_nomi = {}
    def aggiungi_item(self, item):
        """aggiungi item vuol dire che il negozio acquista l'oggetto alla meta del prezzo di vendita
        return -1 se impossibile l'acquisto"""
        prezzo = item.prezzo * 0.5
        if(self.denaro < prezzo):
            return -1
        # NON POSSONO ESISTE DUE ITEM CON LO STESSO NOME E PREZZI DIVERSI
        if(item.nome in self.diz_nomi):
            if(item not in self.inventory.inventario.keys()):
                return -1
        else:
            self.diz_nomi[item.nome] = item ##se non è nel dizionario dei nomi allora lo aggiungo 
        self.inventory.aggiungiItem(item)
        self.denaro -= prezzo
        return 0
    def vendi_item(self, item):
        """vende l'item all'utente, ritorna -1 se non abbastanza item"""
        if(self.inventory.rimuoviItem(item) == -1): 
            return -1
        self.denaro += item.prezzo
        return 0
    def mostra_item(self):
        str = ""
        for i in self.inventory.inventario.keys():
            if(self.inventory.inventario[i] > 0):
                str += f"{i} q.ta {self.inventory.inventario[i]}\n"
        return str
    def cerca_item(self, nome):
        return self.diz_nomi[nome]