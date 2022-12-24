from statistics import mean
from typing import List
from Node import Node
import BKalgorithms

# vertices que tem ligações com todos os vertices de R
P: List[Node] = []

### lendo o arquivo
f = open("./soc-dolphins.mtx", "r")

# verifica se o vertice já esta dentro de uma lista de instancias de Node, pelo nome (string)
def isIn(name: str, Li: List[Node]):
    isInto = False
    for l in Li:
        if l.name == name:
            isInto = True
            break
    return isInto

### colocando os vertices em P
Pstr: list = [str] # lista com os nomes dos vetores em P
for i, n in enumerate(f):
    
    if(i > 35): # pula os comentarios
        line = n.split(' ')
        
        v = Node(line[0])
        
        # verifica se o vertice da esquerda ja não esta em P
        isInto = isIn(v.name, P)
        if(not isInto):
            P.append(v)

        v = Node(line[1][:-1]) # tira o \n no final das linhas
        
        # verifica se o vertice da esquerda ja não esta em P
        isInto = isIn(v.name, P)
        if(not isInto):
            P.append(v)

### retorna os vizinhos do vertice
def getNeighbors(v: str) -> list:
    
    N:list = []
    Nstr:list = [str]

    f.seek(0) # volta o curso para o inicio
    for i, n in enumerate(f):
        
        if i > 35:
            line = n.split(" ")

            line[1] = line[1][:-1] # tira o \n no final das linhas

            # verifica se o vertice da esquerda é igual ao vertice dado e se seu vizinho já nao esta em N. Caso sim, coloca a instacia Node do vertice na lista
            if line[0] == v and not isIn(line[1], N):
                for p in P:
                    if(p.name == line[1]):
                        N.append(p)

            # verifica se o vertice da direita é igual ao vertice dado e se seu vizinho já nao esta em N. Caso sim, coloca a instacia Node do vertice na lista
            if line[1] == v and not isIn(line[0], N):
                for p in P:
                    if(p.name == line[0]):
                        N.append(p)
    return N

### coloca os vizinhos no atributo 'neighbors' dos vertices e calcula o coeficiente de aglomeração do nó
coef_Aglo_i = []
for v in P:
    v.neighbors = getNeighbors(v.name)

    tam = len(v.neighbors)

    if(tam <= 1):
        coef_Aglo_i.append(0)
    else:
        coef_Aglo_i.append(2 / (tam * tam-1))

# chama o algoritmo Bron Kerbosch sem pivo e printa o resultado
print("\nSem pivo:", BKalgorithms.BKnoPivot(P))

# chama o algoritmo Bron Kerbosch com pivo e printa o resultado
print("\nCom pivo:", BKalgorithms.BKPivot(P))

# Coeficiente de Aglomeração do grafo
print("\nCoeficiente de Aglomeração:", mean(coef_Aglo_i))
