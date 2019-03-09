from grafo import *
from priority import *
import time

class d_Heap(CodaPriorita):
    def __init__(self,list,type):
        self.d = type
        self.heap = []
        self.heapLen = len(list)
        self.buildHeap(list)

    def print(self):
        print(self.heap)

    def swap(self,a,b):
        app = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = app

    def estraiRadice(self):
        self.swap(1,len(self.heap)-1)
        rad = self.heap.pop(len(self.heap)-1)
        self.muoviBasso(1)
        return rad

    def genitore(self,a):
        if(a==1):
            return 1
        return int((a+(self.d-2))/self.d) #GENITORE

    def buildHeap(self, list):  # OLD
        self.heap = [None]
        for i in range(0, len(list)):
            self.heap.append(list[i])
            j = i + 1
            while (self.heap[j] < self.heap[self.genitore(j)]):
                self.swap(j, self.genitore(j))
                if (j > 1):
                    j = int((j+(self.d-2))/self.d)  #GENITORE

    def minore(self, list): #restituisce la posizione del minore degli elementi della list
        if(len(list)==0):
            return None
        pos_min = list[0]
        for i in range(1,len(list)):
            if(self.heap[list[i]]<self.heap[pos_min]):
                pos_min = list[i]
        return pos_min

    def figli(self,nodo): #restituisce la lista dei figli del nodo in input
        listaFigli = []
        for i in range(0,self.d):
            if(self.d*nodo-(self.d-(2+i))<len(self.heap)):
                listaFigli.append(self.d*nodo-(self.d-(2+i)))
        return listaFigli

    def muoviBasso(self,v): #se esiste, scambio v con il minore dei figli che e' < v
        if (v <((len(self.heap)+(self.d-2))/self.d)):
            figlio_min = self.minore(self.figli(v))
            if(self.heap[figlio_min]<self.heap[v]):
                self.swap(figlio_min,v)
            self.muoviBasso(figlio_min)

    def muoviAlto(self,v): #se il genitore di v e' maggiore di v li scambio
        while(v!=1 and self.heap[v][0]<self.heap[self.genitore(v)][0]):
            self.swap(v,self.genitore(v))
            v = self.genitore(v)

    #decremento il valore del nodo e della quantita d   O(log_d(n))
    def decreaseKey(self,e,d):
        for i in range(1,len(self.heap)):
            if(self.heap[i][1]==e):
                self.heap[i][0] -= d
                self.muoviAlto(i)
                break

    #incremento il valore del nodo e della quantita d   O(d*log_d(n))
    def increaseKey(self,e,d):
        for i in range(1, len(self.heap)):
            if (self.heap[i][1] == e):
                self.heap[i][0] += d
                self.muoviBasso(i)
                break

    def insert(self,e,k):
        self.heap.append([k,e])
        self.muoviAlto(len(self.heap)-1)

    def delete(self,k):
        self.swap(k, len(self.heap) - 1)
        self.heap.pop(len(self.heap) - 1)
        self.muoviBasso(k)
        #self.muoviAlto(k)


    def prossimo(self): #restituisce al chiamante il valore corrispondente al prossimo nodo da processare
        return self.estraiRadice()[1]



class BinaryHeap(d_Heap):
    def __init__(self,list,type):
        self.d = 2 #d-heap
        self.heap = []
        self.heapLen = len(list)
        self.buildHeap(list)

"""
class HeapBinomiale(d_Heap):
    def __init__(self,list):
        lista_radici = []
        self.d = 2
        self.buildHeap(list)
        self.print() #debug

    def buildHeap(self, list):  # OLD
        pass

    def ristruttura(self):
        pass

    def merge(self,c1,c2):
        pass

"""

def performanceHeap(nNodi):
    # performance heap
    print("\n#####################\nConfronto Performance d-Heap con d = {2,3,5,7}:")
    numeroNodi = nNodi
    lista = []
    for i in range(0, numeroNodi):
        lista.append([randint(-500, 500), "x"])
        d = [2, 3, 5, 7]
    for j in range(0, len(d)):
        start = time.time()
        prova = d_Heap(lista, d[j])
        for i in range(0, len(lista)):
            prova.prossimo()
        end = time.time()
        tempo = round((end - start), 2)
        print("Costruzione Heap ed estrazione radice con", numeroNodi, "nodi tramite", d[j], "\b-Heap: ", tempo,
              "secondi.")



if __name__ == "__main__":

    #prova funzionamento Heap
    lista = [[1,"a"], [2,"b"], [3,"c"], [4,"d"],[5,"e"],[6,"f"],[7,"g"],[8,"h"],[9,"i"],[10,"j"]]

    print("Inserisco la lista",lista,"in un heap:")
    time.sleep(3)

    albero = d_Heap(lista,2) #d = 2 heap binario
    albero.print()
    time.sleep(3)

    print("Estraggo la radice: ")
    time.sleep(2)
    print(albero.prossimo())
    time.sleep(2)
    print("heap aggiornato: ")
    time.sleep(2)

    albero.print()
    time.sleep(2)
    print("Decremento la chiave dell'elemento e per 5 volte: ")
    albero.decreaseKey("e",5)
    time.sleep(3)

    albero.print()
    time.sleep(3)
    print("estraggo la radice per 3 volte: ")
    time.sleep(2)
    print(albero.prossimo())
    time.sleep(1)
    print(albero.prossimo())
    time.sleep(1)
    print(albero.prossimo())
    time.sleep(3)

    print("albero aggiornato:")
    time.sleep(1)
    albero.print()

    time.sleep(2)
    print("Incremento d per 7 volte")
    albero.increaseKey("d",7)
    time.sleep(3)
    albero.print()
    time.sleep(2)
    print("decremento j di 3")
    albero.decreaseKey("j",3)
    time.sleep(2)
    albero.print()
    time.sleep(2)
    print("estraggo la racice per 4 volte")
    time.sleep(2)
    print(albero.prossimo())
    time.sleep(1)
    print(albero.prossimo())
    time.sleep(1)
    print(albero.prossimo())
    time.sleep(1)
    print(albero.prossimo())
    time.sleep(3)
    print("heap aggiornato:")
    time.sleep(3)
    albero.print()







