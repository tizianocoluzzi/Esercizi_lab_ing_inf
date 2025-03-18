from abc import ABC, abstractmethod
import random
class GenericItem(ABC):
    @abstractmethod
    def tempo_spedizione(self)->str:
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    def __repr__(self):
        return str(self) #totalmente sbaglito ma per stampare i Dict mi chiama repr e allora io so stronzo e faccio cosi