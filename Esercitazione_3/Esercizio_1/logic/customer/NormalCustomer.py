from ..customer.GenericCustomer import GenericCustomer
from ..store_item.GenericItem import GenericItem
class NormalCustomer(GenericCustomer):
    def __init__(self, nome:str, budget:int)->None:
        super().__init__(nome, budget)
    
    def acquisto(self, store_item: GenericItem)->bool:
        """acquisto di un item
        return values: 
            False se non abbastanza budget 
            True se anadato a buon fine"""
        if self.b < store_item.prezzo :
            return False
        else: 
            # controllo se l'elemento è gia posseduto 
            if(store_item in self.items):
                self.items[store_item] += 1
            else:
                self.items[store_item] = 1
            self.b -= store_item.prezzo
        return True
    
       


