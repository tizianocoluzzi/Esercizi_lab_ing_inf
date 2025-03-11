from customer.GenericCustomer import GenericCustomer
class NormalCustomer(GenericCustomer):
    def __init__(self, nome, budget):
        self.nome = nome
        self.b = budget
    def acquisto(self, store_item):
        """acquisto di un item
        return values: 
            -1 se non abbastanza budget 
            0 se anadato a buon fine"""
        if self.b < store_item.prezzo :
            return -1
        else: 
            self.b -= store_item.prezzo
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


