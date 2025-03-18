from store_item.GenericItem import GenericItem
class StoreInventory:
    def __init__(self):
        self.inventario = {}
    def aggiungiItem(self, item:GenericItem)->None:
        """aggiunge un elemento all'inventario"""
        if(item in self.inventario.keys()):
            self.inventario[item] += 1
        else:
            self.inventario[item] = 1
    def rimuoviItem(self, item:GenericItem)->bool:
        """rimuove un elemento, se non esiste ritorna False"""
        if(item in self.inventario and self.inventario[item] > 0):
            self.inventario[item] -= 1
            return True
        else:
            return False
    