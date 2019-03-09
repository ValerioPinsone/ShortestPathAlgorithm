#importo la classe per la gestione di matrici
#from grafo import *
from heap import *
import time


def nonPresente(n,list): #Controllo se n e' stato gia' processato
    if len(list)==0:
        return 1
    for i in range(0,len(list)):
        if(n==list[i]):
            return 0
    return 1

#algoritmo ricorsivo di visita DFS
def visita(G,v,o):
    ord = o
    cont = 0
    G.visitato[v] = 1
    for i in G.adiacente(v):
        if not G.visitato[i]:
            ord = [i] + visita(G,i,ord)
    return ord

def ordinamentoTopologicoDFS(G,s):
    for i in range(s,G.numV()): #cerco un nodo con 0 archi entranti
        if(len(G.incidente(i))==0 and not G.visitato[i]): #se il numero di archi entranti e' == 0
            return [i] + visita(G,i,[]) #ritorno la visita DFS per l'ordinamento top.


def ordinamentoTopologico(G):
    G.azzeraVisitati()
    l = []
    s2 = 0
    while(len(l)!=G.numV()):
        #l += ordinamentoTopologicoDFS(G,s2)
        #if(s2 not in G.visitato):   #agg
        l = ordinamentoTopologicoDFS(G,s2) + l
        #G.visitato.append(s2) #agg
        s2 += 1
    ord = []
    for i in range(0,len(l)):
        ord.append([i,l[i]])
    return ord

def BellmanFord(G,s):
    G.resetPesi()
    G.inizializzaPesi(s)  # inizializzo le distanze (0 se v==s altrimenti Inf)
    stabile = 0
    for k in range(0,G.numV()-1):
        for i in range(0, G.numV()):
            for v in range(0, G.numV()):
                if (G.esistenzaArco(i, v) and v != s):
                    if (G.Peso(i) + G.distanza(i, v) < G.Peso(v)):
                        G.aggiornaPeso(v, (G.Peso(i) + G.distanza(i, v)))  # rilassamento
    return G.listaPesi()

def distanzeAciclicoOld(G,s,d):
   G.resetPesi()
   G.inizializzaPesi(s) #inizializzo le distanze (0 se v==s altrimenti Inf)
   topologicoStd = ordinamentoTopologico(G)
   ord = d_Heap(topologicoStd,d) #d = 2,3,5,7

   for i in range(0,G.numV()):
       nodo = ord.prossimo()
       for v in range(0,G.numV()):
        if(G.esistenzaArco(nodo,v) and v!=s):# and i!=v): #aggiunto ultimo and (controllare correttezza)
            if(G.Peso(nodo)+G.distanza(nodo,v)<G.Peso(v)):
                G.aggiornaPeso(v,(G.Peso(nodo)+G.distanza(nodo,v))) #rilassamento
   return G.listaPesi()

def prelevaNodi(G):
    nodi = []
    for i in range(0,G.numV()):
        nodi.append([G.numIncidenti(i),i]) #key value
    return nodi

def distanzeAciclico(G,s,d):
   G.resetPesi() #aggiunto
   G.inizializzaPesi(s) #inizializzo le distanze (0 se v==s altrimenti Inf)
   #D = G.listaPesi()
   #G.azzeraVisitati()
   listaNodi = prelevaNodi(G)
   ord = d_Heap(listaNodi,d) #d = 2,3,5,7

   for i in range(0,G.numV()):
       nodo = ord.prossimo()
       adiacenti = G.adiacente(nodo)
       for j in range(0, len(adiacenti)):
           ord.decreaseKey(adiacenti[j], 1)
       for v in range(0,G.numV()):
        if(G.esistenzaArco(nodo,v) and v!=s):# and i!=v): #aggiunto ultimo and (controllare correttezza)
            if(G.Peso(nodo)+G.distanza(nodo,v)<G.Peso(v)):
                G.aggiornaPeso(v,(G.Peso(nodo)+G.distanza(nodo,v))) #rilassamento
   return G.listaPesi()




#Debug
if __name__ == "__main__":
    #Grafo presente al capitolo 14 del libro di testo
    grafo1 = Grafo(7)

    grafo1.inserimentoRapido([
        [0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0]
    ])



    ###esempio funzionamento####

    dim = int(input("Inserisci dimensione grafo: "))
    print("Genero grafo acilico di dimensione",dim)
    grafo2 = Grafo(dim)
    grafo2.generaAciclico()
    grafo2.stampa()
    time.sleep(0.5)
    ric = "Da quale vertice calcolare la distanza? (0-"+str(dim-1)+"): "
    v = -1
    while(v<0 or v>(dim-1)):
        v = int(input(ric))

    print("\nDistanze Tramite Bellman-Ford:")
    print(BellmanFord(grafo2,v))
    #print(distanzeAciclicoOld(grafo2,0,2))
    print("\nDistanze Tramite distanceAciclico:")
    print(distanzeAciclico(grafo2, v, 2)) #d-heap d = 2



