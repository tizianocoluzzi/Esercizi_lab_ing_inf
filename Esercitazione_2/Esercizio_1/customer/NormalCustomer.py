from customer.GenericCustomer import GenericCustomer
from store_item.GenericItem import GenericItem
class NormalCustomer(GenericCustomer):
    def __init__(self, nome:str, budget:int)->None:
        self.nome = nome
        self.b = budget
    
    def acquisto(self, store_item: GenericItem)->bool:
        """acquisto di un item
        return values: 
            False se non abbastanza budget 
            True se anadato a buon fine"""
        if self.b < store_item.prezzo :
            return False
        else: 
            self.b -= store_item.prezzo
        return True
    
    def accredito(self, somma:int)->bool:
        """accredito di somma
            Return values:
                False se somma <= 0
                True se andato a buon fine"""
        if (somma > 0):
            self.b+=somma
            return True
        return False


