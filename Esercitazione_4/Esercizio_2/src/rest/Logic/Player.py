from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self, nome, max_num):
        self.nome = nome
        self.max_num = max_num
        self.tentativi = 0
        self.mmu: int
    @abstractmethod
    def guess(self):
        pass
    def check_guess(self, mmu):
        self.mmu = mmu      
    def reset(self, max_num):
        self.tentativi = 0
        self.max_num = max_num
class HumanPlayer(Player):
    def __init__(self, nome, max_num):
        super().__init__(nome, max_num)

    def guess(self):
        try:
            print("scegli numero:")
            x = int(input())
            self.tentativi += 1
        except ValueError:
            print("non è stato inserito un numero, riprova:")
            x = self.guess()
        finally:
            return x

class CpuPlayer(Player):
    def __init__(self, nome,max_num):
        super().__init__(nome,max_num)
        self.old_guess = max_num / 2
    def guess(self):
        if(self.tentativi == 0): 
            self.tentativi += 1
            return self.old_guess
        self.tentativi += 1
        if(self.mmu < 0):
            self.old_guess +=1
        elif(self.mmu > 0):
            self.old_guess -= 1
        else:
            print("Ho vinto")
        return self.old_guess
class FastPlayer(Player):
    def __init__(self, nome, max_num):
        super().__init__(nome, max_num)
        self.old_guess = max_num / 2
        self.min_num = 0
    def guess(self):
        if(self.tentativi == 0): 
            self.tentativi += 1
            return self.old_guess
        self.tentativi += 1
        if(self.mmu < 0):
            #andare verso numeri piu grandi
            self.min_num = self.old_guess + 1
        elif(self.mmu > 0):
            #andare verso numeri piu piccoli
            self.max_num = self.old_guess -1
        else:
            print("Ho vinto")
        self.old_guess = (self.max_num + self.min_num)/2
        return int(self.old_guess)
    def reset(self, max_num):
        super().reset(max_num)
        self.min_num = 0