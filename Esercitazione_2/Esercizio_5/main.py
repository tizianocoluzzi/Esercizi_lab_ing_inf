import random
import time
import matplotlib.pyplot as plt 
from typing import List, Dict

'''esercizio banchmark libreria standard'''

PATH = 'result.csv'
times_list: List[float] = []
times_set: List[float] = []
dims: List[int] = []

def create_random_set(dim: int):
    '''restituisce un set di elementi casuali di dimensione dim'''
    l = set()
    for i in range(0, dim, 1):
        l.add(random.randint(0, dim*2))
    return l
def create_random_list(dim: int) -> List[int]:
    l: List[int] = []
    for i in range(0, dim, 1):
        l.append(random.randint(0, dim*2))
    return l
    '''restituisce una lista di elementi casuali di dimensione dim'''

def populate_file():
    '''popola il file'''
    for i in range(0, 1000, 1):
        dim = i * 10
        for j in range(0, 10, 1):
            s1 = 0
            s2 = 0
            l1 = create_random_list(dim)
            l2 = create_random_set(dim)
            x = random.randint(0, dim*2)
            # calcolo del tempo su lista
            t1i = time.perf_counter()
            x in l1
            t1f = time.perf_counter()
            t1 = t1f - t1i
            # calcolo del tempo su set 
            t2i = time.perf_counter()
            x in l2
            t2f = time.perf_counter()
            t2 = t2f - t2i
            # somma dei valori dei tempi
            s1 += t1
            s2 += t2
        
        times_list.append(s1/10) #aggiunge la media dei tempi
        times_set.append(s2/10)
        dims.append(dim) 
        with open (PATH, "a") as f:
            f.write(f"{dim},{s1/10},{s2/10}\n")

if __name__ == '__main__':
    try:
        f = open(PATH, "r")
        for i in f.readlines():
            l = i.split(",")
            dims.append(int(l[0]))
            times_list.append(float(l[1]))
            times_set.append(float(l[2]))

    except FileNotFoundError:
        populate_file()
    plt.plot(dims, times_list)
    plt.plot(dims, times_set)
    plt.ylabel("tempo")
    plt.xlabel("dimensione")
    plt.show()   
    pass