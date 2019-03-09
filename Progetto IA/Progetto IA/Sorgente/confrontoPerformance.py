from algoritmo import *

d = [2,3,5,7]
#numNodi = [20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
numNodi = []

for i in range(1,100):
    numNodi.append(10*i)

for i in range(0,len(numNodi)):
    print("\n############## ", numNodi[i], " vertici ################")
    start = time.time()
    grafo = Grafo(numNodi[i])
    grafo.generaAciclico()
    end = time.time()
    print("\nGenerato in",round(end-start,2),"Secondi")
    for j in range(0,len(d)):

        start = time.time()
        distanzeAciclico(grafo,0,d[j])#calcolo distanze a partire dal nodo 0
        end = time.time()
        print("Tempo di esecuzione su grafo con", numNodi[i] ,"nodi tramite",d[j],"\b-Heap: ",round(end-start,3),"secondi")

    start = time.time()
    distanzeAciclicoOld(grafo, 0,2)  # calcolo distanze a partire dal nodo 0
    end = time.time()
    print("Tempo di esecuzione su grafo con", numNodi[i], "nodi tramite Ordinamento Topologico DFS: (2-Heap)", round(end - start, 3),"secondi")

    start = time.time()
    BellmanFord(grafo, 0)  # calcolo distanze a partire dal nodo 0
    end = time.time()
    print("Tempo di esecuzione su grafo con", numNodi[i], "nodi tramite Bellman-Ford: ", round(end - start, 3),"secondi")








