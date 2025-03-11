from abc import ABC, abstractmethod
#RICORDA 0 negativo 1 positivo
class Model(ABC):
    @abstractmethod
    def predict(self, file):
        pass
class BasicModel(Model):
    def __init__(self, file):
        """file è il file su cui è stato addestrato"""
        self.file = file
        self.risposta = self.stima()
    
    def predict(self, file):
        """predice il risultato per ogni riga e stampa l'accuracy totale del file"""
        with open(file, "r", encoding='UTF-8') as f:
            s = 0
            linee = 0
            f.readline() #salto la prima
            while(True):
                try:
                    current = int(f.readline().split(",")[-1])
                except ValueError:
                    break
                linee += 1
                if self.risposta == current:
                    s += 1
            print(f"accuracy: {s/linee}")
                

    def stima(self):
        with open(self.file, "r", encoding='UTF-8') as f:
            result = 0
            current = f.readline() # salto la prima che è superflua
            linee = 0
            while(current != ""):
                linee += 1
                current = f.readline().split(",")[-1]
                try:
                    result += int(current)
                except ValueError:
                    break
            #se il risultato è minore del 50% il modello restituisce sempre negativo
            if(result/linee < 0.5):
                return 0
            else:
                return 1 
class WordModel(Model):
    def __init__(self):
        pass
    def predict(self, file):
        p_count = 0
        n_count = 0
        p = positive_set()
        n = negative_set()
        #p = {"good", "well", "better", "amazing"}
        #n = {"bad", "worst", "horrible", "absurd"}
        lines = 0
        tot = 0 
        with open(file, "r", encoding='UTF-8') as f:
            f.readline() #skippo la prima
            while(True):
                n_count = 0
                p_count = 0
                frase = f.readline()
                lines += 1
                ws = frase.split(" ")
                for i in ws:
                    if(i in p):
                        p_count +=1
                    elif(i in n):
                        n_count += 1
                if n_count > p_count:
                    res = 0
                else:
                    res = 1
                result = frase.split(",")[-1]
                #print(f"negative: {n_count} positive: {p_count}")
                try:
                    if(res == int(result)):
                        tot +=1
                except ValueError:
                    break
        print(f"accuracy:{tot/lines}")  
def positive_set():
    ins = set()
    l = open("positive_words.tsv", "r", encoding='UTF-8')
    for i in l:
        ins.add(i[0:-1]) #taglia l'ultima lettera
    return ins
def negative_set():
    ins = set()
    l = open("negative_words.tsv", "r", encoding='UTF-8')
    for i in l:
        ins.add(i[0:-1])
    return ins

if __name__ == '__main__':
    model = BasicModel("recensioni_add.csv");
    model.predict("recensioni_test.csv")
    model2 = WordModel()
    model2.predict("recensioni_test.csv")