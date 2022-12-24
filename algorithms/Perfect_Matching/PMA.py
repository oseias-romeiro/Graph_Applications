from Hall_Theorem import Hall_Theorem

X = {
    'A': [[0, 2],[1, 4],[2, 6]],
    'B': [[2, 1],[0, 3],[1, 5]],
    'C': [[0, 4],[2, 5],[1, 7]],
}
Y = {# with vedge alues
    0: [['A', 2, False], ['B', 3, False], ['C', 4, False]],
    1: [['A', 4, False], ['B', 5, False], ['C', 7, False]],
    2: [['B', 1, False], ['C', 5, False], ['A', 6, False]],
}

print(f"Exist a perfect mathcing? {Hall_Theorem(X)}")

def get_max_value(negihbors: list):
    max_value = 0
    vertice = ''

    for n in negihbors:
        if(n[1] > max_value):
            max_value = n[1]
            vertice = n[0]
    
    return vertice

def is_matching(negihbors: list):
    for n in negihbors:
        if(n[2] == True):
            return n
    return False

def match(negihbors: list, vertice):
    for n in negihbors:
        if(n[0] == vertice):
            n[2] = True
            break

def matching_value(negihbors: list, vertice):
    for n in negihbors:
        if(n[0] == vertice):
            return n[1]

def remove(y, x: list):
    i = 0
    for n in x:
        if(n[0] == y):
            break
        i += 1
    x.pop(i)

def swip(neighbors: list, currently_match: list, x):
    for n in neighbors:
        if(n == currently_match):
            n[2] = False
        if(n[0] == x):
            n[2] = True

def PMA(X: dict, Y: dict):
    queue = list(X.keys())

    while len(queue) != 0:
        x = queue.pop(0)
        queue.append(x)

        try:
            y = Y[get_max_value(X[x])]
        except:
            break
        

        y_match = is_matching(y)
        if(y_match):
            if(y_match[1] < matching_value(y, x)):
                print(y, y_match, x)
                swip(y, y_match, x)
                print(y)
                queue.append(x)
            else:
                for k in Y.keys():
                    if(Y[k] == y):
                        remove(k, X[x])
                        break
        else:
            match(y, x)
    
    return Y

print(PMA(X, Y))
