from customer.GenericCustomer import GenericCustomer
class PromotionalCustomer(GenericCustomer):
    def __init__(self, nome, budget:int):
        self.nome = nome
        self.b = budget
        self.sconto = 0.05
    def acquisto(self, store_item):
        """acquisto di un item
        return values: 
            -1 se non abbastanza budget 
            0 se anadato a buon fine"""
        prezzo = store_item.prezzo - store_item.prezzo*self.sconto 
        if self.b < prezzo :
            return -1
        else: 
            self.b -= prezzo
        return 0
    def accredito(self, somma):
        """accredito di somma
            Return values:
                -1 se somma <= 0
                0 se andato a buon fine"""
        if (somma > 0):
            self.b+=somma
            return 0;
        return -1;


