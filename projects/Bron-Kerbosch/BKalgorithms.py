
from typing import List


def BKnoPivot(P: list, R: list = [], X: list = [], maximais: list = []) -> List[list]:

    if(len(P) == 0 and len(X) == 0):
        maximais.append(R)

        return maximais

    for v in P:
        Rnew = R + [v]
        Pnew = [n for n in P if n in v.neighbors]
        Xnew = [n for n in X  if n in v.neighbors]

        maximais = (BKnoPivot(Pnew, Rnew, Xnew, maximais))

        P.remove(v)
        X.append(v)

    return maximais

def BKPivot(P: list, R: list = [], X: list = [], maximais: list = []) -> List[list]:

    if(len(P) == 0 and len(X) == 0):
        maximais.append(R)

        return maximais

    u = (P + X)[0]
    P2 = []
    for p in P:
        if(p not in u.neighbors):
            P2.append(p)

    for v in P2:
        Rnew = R + [v]
        Pnew = [n for n in P if n in v.neighbors]
        Xnew = [n for n in X  if n in v.neighbors]

        maximais = BKPivot(Pnew, Rnew, Xnew, maximais)

        P.remove(v)
        X.append(v)

    return maximais