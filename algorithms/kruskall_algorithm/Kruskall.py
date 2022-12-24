## Prim algorithm: Minimum spanning trees

# vertices with neighbors and its weights

V = {
    'A': [['B', 7], ['D', 5]],
    'B': [['A', 7], ['C', 8], ['D', 9], ['E', 7]],
    'C': [['B', 8], ['E', 5]],
    'D': [['A', 5], ['B', 9], ['E', 15], ['F', 6]],
    'E': [['B', 7], ['C', 5], ['D', 15], ['F', 8], ['G', 9]],
    'F': [['D', 6], ['E', 8], ['G', 11]],
    'G': [['F', 11], ['E', 9]]
}

E = {'A-B': 7, 'A-D': 5, 'B-C': 8, 'B-D': 9, 'B-E': 7, 'C-E': 5, 'D-E': 15, 'D-F': 6, 'E-F': 8, 'E-G': 9, 'F-G': 11}

# ordering edges
def ordEdges(E: dict) -> list:
    Eord = []

    while len(E) > 0:
        smaller = float("Inf")
        key = ''
        for e in E:
            if(E[e] < smaller):
                smaller = E[e]
                key = e
        
        Eord.append(key)
        E.pop(key)

    return Eord

# kruskall
def kruskall(E: dict):
    # vertices
    S = []
    # edges
    T = []

    Eord = ordEdges(E)

    while len(Eord) > 0:

        v = Eord.pop(0).split('-')

        if(v[0] not in S or v[1] not in S):
            T.append(v[0] + '-' + v[1])
        elif(v[0] in S and v[1] in S):
            # detecta ciclo
            pass

        if(v[0] not in S):
            S.append(v[0])
        
        if(v[1] not in S):
            S.append(v[1])

    return S,T

S,T = kruskall(E)

print('S:',S)
print('T:',T)
