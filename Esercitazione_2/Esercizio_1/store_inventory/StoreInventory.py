class StoreInventory:
    def __init__(self):
        self.inventario = {}
    def aggiungiItem(self, item):
        """aggiunge un elemento all'inventario"""
        if(item in self.inventario.keys()):
            self.inventario[item] += 1
        else:
            self.inventario[item] = 1
    def rimuoviItem(self, item):
        """rimuove un elemento, se non esiste ritorna -1"""
        if(item in self.inventario and self.inventario[item] > 0):
            self.inventario[item] -= 1
            return 0
        else:
            return -1
    