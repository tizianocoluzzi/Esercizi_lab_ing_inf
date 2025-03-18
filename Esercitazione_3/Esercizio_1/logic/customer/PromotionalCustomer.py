from ..customer.GenericCustomer import GenericCustomer
from ..store_item.GenericItem import GenericItem
class PromotionalCustomer(GenericCustomer):
    def __init__(self, nome, budget:int)->None:
        super().__init__(nome, budget)
        self.sconto = 0.05
    def acquisto(self, store_item)->bool:
        """acquisto di un item
        return values: 
            False se non abbastanza budget 
            True se anadato a buon fine"""
        prezzo = store_item.prezzo - store_item.prezzo*self.sconto 
        if self.b < prezzo :
            return False
        else: 
            if(store_item in self.items):
                self.items[store_item] += 1
            else:
                self.items[store_item] = 1
            self.b -= prezzo
        return True


