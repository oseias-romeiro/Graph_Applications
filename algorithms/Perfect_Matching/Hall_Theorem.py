from itertools import combinations

# return if a set with vertices and neighbors is has a perfect matching
def Hall_Theorem(X: dict) -> bool:
    keys = list(X.keys())
    i = 1
    # reach all subgroups possible of X
    while i != len(X):
        for subgroup in combinations(range(len(X)), i):
            # catch all neighbors of each vertices in group
            neighbors = 0
            for s in subgroup:
                neighbors += len(X[keys[s]])
            # verify if the set neighbors is smaller than set length of combinaion
            if(neighbors < i):
                return False
        i += 1
    return True
