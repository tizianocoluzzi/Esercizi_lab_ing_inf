from abc import ABC, abstractmethod
from store_item.GenericItem import GenericItem
class GenericCustomer(ABC):
    """class to generalize a customer"""
    @abstractmethod
    def acquisto(self, store_item:GenericItem)->bool:
        pass
    @abstractmethod
    def accredito(self, somma:int)->bool:
        pass
