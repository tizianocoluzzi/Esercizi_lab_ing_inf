from abc import ABC, abstractmethod
class GenericCustomer(ABC):
    """class to generalize a customer"""
    @abstractmethod
    def acquisto(self, store_item):
        pass
    @abstractmethod
    def accredito(self, somma):
        pass
