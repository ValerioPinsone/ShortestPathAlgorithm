
#importo math per utilizzare una rappresentazione di infinito
import math
import time
from random import *
#Definisco la classe grafo con n vertici ed m archi
#n = |V| m = |E|
#Spazio: O(|V|^2) Controllo Adiac.: O(1)
class Grafo:
    def __init__(self,n):
        self.mat = []
        self.pesi = []
        self.visitato = []
        self.vertici = n
        self.archi = 0
        self.inizializza(0)
        #self.stampa() #debug


    #inizializzo la matrice a val
    def inizializza(self,val):
        self.mat = []
        for i in range(0,self.vertici):
            self.visitato.append(0)
            self.mat.append([])
            for j in range(0,self.vertici):
                self.mat[i].append(val)

    def azzeraVisitati(self):
        self.visitato = []
        for i in range(0,self.numV()):
            self.visitato.append(0)

    #inizializza i pesi a inf e la sorgente a 0
    def inizializzaPesi(self,v):
        for i in range(0,self.vertici):
            self.pesi.append(math.inf)
        self.pesi[v] = 0
    def listaPesi(self):
        return self.pesi

    #reset della lista pesi
    def resetPesi(self):
        self.pesi = []

    #aggiorna il peso di un nodo con il valore val
    def aggiornaPeso(self,nodo,val):
        self.pesi[nodo] = val

    #restituisce il peso del nodo n
    def Peso(self,n):
        return self.pesi[n]

    #metodo per la stampa a schermo della matrice
    def stampa(self):
        print("-----------------")
        for row in self.mat:
            print(row)

    #inserisce in posizione (x,y) il valore v
    #x adiacente y con peso v
    def inserisci(self,x,y,v):
        self.mat[x][y] = v
        self.archi = self.numE()

    #azzera la riga n della matrice di adiacenza
    def azzeraRiga(self,n):
        for i in range(0,self.vertici):
            self.mat[n][i] = 0

    #restituisce true se il grafo non ha archi
    def nessunArco(self):
        for i in range(0,self.vertici):
            for j in range(0, self.vertici):
                if(self.mat[i][j]!=0):
                    return False
        return True

    #restituisce il numero di vertici
    def numV(self):
        return self.vertici

    #restotuisce il numero di archi
    def numE(self):
        n = 0
        for i in range(0,self.vertici):
            for j in range(0,self.vertici):
                if(self.mat[i][j]!=0):
                    n+= 1
        return n

    #restituisce il grado di un nodo
    def gradoV(self,x):
        if(self.pesi):
            return self.pesi[x]
        else:
            return None

    #restituisce i vertici adiacenti al vertice a
    def adiacente(self,a):
        ad = []
        for i in range(0,self.vertici):
            if(self.mat[a][i]!=0):
                ad.append(i)
        return ad

    #restituisce i vertici incidenti al vertice a
    def incidente(self, a):
          ad = []
          for i in range(0,self.vertici):
              if(self.mat[i][a]!=0):
                  ad.append(i)
          return ad

    #restituisce il numero di archi incidenti ad a
    def numIncidenti(self, a):
          num = 0
          for i in range(0,self.vertici):
              if(self.mat[i][a]!=0):
                  num += 1
          return num

    #restituisce la distanza per arrivare da a a b
    def distanza(self,a,b):
        if(self.mat[a][b]==0):
            return math.inf
        return self.mat[a][b]

    def getMatrix(self):
        return self.mat

    #genera rapidamente un grafo a partire da una matrice
    def inserimentoRapido(self,m):
        dim = int(len(m[0]))
        for i in range(0,dim):
            for j in range(0,dim):
                self.inserisci(i,j,m[i][j])

    #controlla l'esistenza di un arco a -> b
    def esistenzaArco(self,a,b):
        if(self.mat[a][b]!=0):
            return 1
        return 0

    #test1: poco performante
    def generaAciclico(self): #genera grafo aciclico con pesi random
        listaNodi = []        #lista dei nodi da inserire
        nodiEstratti = []     #lista dei nodi estratti
        rangePesi = 100       #range pesi                                                       SETTING 1
        maxArchiUscenti = 10   #imposto il numero massimo degli archi uscenti da un nodo        SETTING 2

        #riempio la lista nodi
        for i in range(0,self.numV()):
            listaNodi.append(i)

        #randomizzo l'ordine dei nodi
        for i in range(0,len(listaNodi)):
            rndr = randint(0,len(listaNodi)-1)
            app = listaNodi[i]
            listaNodi[i] = listaNodi[rndr]
            listaNodi[rndr] = app
            nodoEntr = []

        """
            l'algoritmo genera a ritroso un ordinamento topologico
            per poi costruire la relativa matrice di adiacenza
            in questo modo non e' necessario eseguire un controllo di aciclicita'
            in quanto il grafo risultante rispettera' sicuramente la proprieta'
            (lento all'aumentare del numero di nodi)
        """

        #inizializzo la matrice a 0
        self.inizializza(0)
        #self.stampa() #debug

        for i in range(0,len(listaNodi)):
            nodoEntr = []
            for j in range(0,maxArchiUscenti):
                if(randint(0,5)): #probabilita' di generare un arco              SETTING 3
                    if(len(nodiEstratti)>0):
                        #inserisco nella matrice l'arco dal nodo listaNodi[i] ad un arco random tra quelli estratti con peso random
                        # (sostituire -rangePesi con 0 per ottenere solo pesi positivi)
                        nodo_arr = nodiEstratti[randint(0, len(nodiEstratti) - 1)]
                        if nodo_arr not in nodoEntr:
                            self.inserisci(nodo_arr,listaNodi[i],randint(0, rangePesi))
                            nodoEntr.append(nodo_arr)
            #aggiungo il nodo appena processato alla lista degli estratti rendendolo disponibile a ricevere archi entranti:
            nodiEstratti.append(listaNodi[i])


    #non funzionante
    def generaAciclicoFast(self):
        self.inizializza(0)#inizializzo la matrice a 0

        listaNodi = []  # lista dei nodi da inserire
        rangePesi = 100  # range pesi                                                       SETTING 1
        maxArchiUscenti = 5  # imposto il numero massimo degli archi uscenti da un nodo        SETTING 2
        colonnaVuota = randint(0,self.numV()-1)
        """
        # riempio la lista nodi
        for i in range(0, self.numV()):
            listaNodi.append(i)

        # randomizzo l'ordine dei nodi
        for i in range(0, len(listaNodi)):
            app = listaNodi[i]
            listaNodi[i] = listaNodi[randint(0, len(listaNodi) - 1)]
            listaNodi[randint(0, len(listaNodi) - 1)] = app
        """
        for i in range(0,self.numV()):
            for j in range(0,maxArchiUscenti):
                dest = randint(0,self.numV()-1)
                if(self.mat[dest][i]==0 and i!=dest and i!=colonnaVuota):
                    if(randint(0,1)):
                        self.inserisci(i,dest,1)



if __name__ == "__main__":

    prova = Grafo(int(input("Genera Aciclico con vertici = ")))
    prova.generaAciclico()
    prova.stampa()

    """
    prova.inserimentoRapido([[0,0,1,0],
                            [0,0,1,1],
                            [0,1,1,0],
                            [0,3,0,0]])
    """