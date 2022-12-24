## Prim algorithm: Minimum spanning trees

# vertices with neighbors and its weights

V = {
    'A': [['B', 4], ['H',  8]],
    'B': [['A', 4], ['C',  8], ['H', 11]],
    'C': [['B', 8], ['D',  7], ['F',  4], ['I', 2]],
    'D': [['C', 7], ['E',  9], ['F', 14]],
    'E': [['D', 9], ['F', 10]],
    'F': [['C', 4], ['D', 14], ['E', 10], ['G', 2]],
    'G': [['F', 2], ['H',  1], ['I',  6]],
    'H': [['A', 8], ['B', 11], ['G',  1],  ['I', 7]],
    'I': [['C', 2], ['G',  6], ['H',  7]]
}

# vertices
S = ['A']
# edges
T = []

coast = 0
while True:
    smaller = 999
    next_v = ''
    current_v = ''
    pos = 0
    coast_e = 0

    # search smaller weight in connection with vertex
    for s in S:
        i = 0
        for neighbor in V[s]:
            if(neighbor[1] < smaller):
                smaller = neighbor[1]
                next_v = neighbor[0]
                current_v = s
                pos = i
            i += 1

    # end
    if(smaller >= 999):
        break

    if(next_v not in S):
        # add vertex and edge
        S.append(next_v)
        T.append(current_v+'-'+next_v)
        coast += smaller
    else:
        # add wheight 1000 to vertex to be avoided
        V[current_v][pos] = [next_v, 1000]

# out
print('S:', S)
print('T:', T)
print('coast:', coast)
