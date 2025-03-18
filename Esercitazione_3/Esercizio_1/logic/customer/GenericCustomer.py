from abc import ABC, abstractmethod
from ..store_item.GenericItem import GenericItem
from typing import Dict
class GenericCustomer(ABC):
    """class to generalize a customer"""
    
    def __init__(self, nome:str, budget:int)->None:
        self.nome = nome
        self.b = budget
        self.items: Dict[GenericItem, int] = {}
    
    @abstractmethod
    def acquisto(self, store_item:GenericItem)->bool:
        pass
    def accredito(self, somma:int)->bool:
        """accredito di somma
            Return values:
                False se somma <= 0
                True se andato a buon fine"""
        if (somma > 0):
            self.b+=somma
            return True
        return False
    
    def lista_posseduti(self)->str:
        s = ""
        for i in self.items.items():
            s += f"{i[0]} qta: {i[1]}\n"
        return s
