from abc import ABC, abstractmethod
import random
class GenericItem(ABC):
    @abstractmethod
    def tempo_spedizione(self)->str:
        pass
    
