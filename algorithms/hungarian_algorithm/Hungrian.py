from typing import List
from Element import Element

a = Element(14)
b = Element(5)
c = Element(8)
d = Element(7)
e = Element(2)
f = Element(12)
g = Element(6)
h = Element(5)
i = Element(7)
j = Element(8)
k = Element(3)
l = Element(9)
m = Element(2)
n = Element(4)
o = Element(6)
p = Element(10)

matrix_rows: List[List[Element]] = [
    [a,b,c,d],
    [e,f,g,h],
    [i,j,k,l],
    [m,n,o,p]
]

matrix_cols: List[List[Element]] = [
    [a,e,i,m],
    [b,f,j,n],
    [c,g,k,o],
    [d,h,l,p]
]

def min(li: List[Element]) -> int:
    minor = 9999
    for l in li:
        if(l.getValue() < minor and not l.isCovered()):
            minor = l.getValue()
    
    return minor

def min_all() -> int:
    min_global = 9999
    for row in matrix_rows:
        min_row = min(row)
        if(min_row < min_global):
            min_global = min_row
    
    return min_global

def count_zeros(obj: List[Element]) -> int:
    count = 0
    for e in obj:
        if(e.getValue() == 0):
            count += 1
    
    return count

def all_0_convered() -> bool:
    for row in matrix_rows:
        for e in row:
            if(e.getValue() == 0):
                if(not e.isCovered()):
                    return False
    
    return True

def exist_0_non_convered(li: List[Element]):
    for e in li:
        if(e.getValue() == 0 and not e.isCovered()):
            return True
    
    return False

def print_matrix():
    for row in matrix_rows:
        elemenets = ''
        for e in row:
            if(e.isCovered()):
                elemenets += "~" + str(e.getValue()) + " | "
            else:
                elemenets += " " + str(e.getValue()) + " | "

        print(elemenets)

    print('\n')

# Subtract row minimal
def step1():
    for row in matrix_rows:
        minimal = min(row)
        if(minimal > 0):
            indice = 0
            for e in row:
                row[indice].setValue(e.getValue() - minimal)
                indice += 1

# Subtract column minimal
def step2():
    for col in matrix_cols:
        minimal = min(col)
        if(minimal > 0):
            indice = 0
            for e in col:
                col[indice].setValue(e.getValue() - minimal)
                indice += 1

# Cover all zeros with a minimum number of lines
def step3(len_coveres):
    mat_rows_copy = matrix_cols.copy()
    mat_cols_copy = matrix_rows.copy()

    while not all_0_convered():
        toCover: List[Element] = []
        row_col_i = []

        max_zeros = 0
        ri = 0
        for row in mat_rows_copy:
            count_zero = count_zeros(row)
            if(count_zero > max_zeros and exist_0_non_convered(row)):
                max_zeros = count_zero
                toCover = row
                row_col_i = ["row", ri]
            ri += 1
        
        ci = 0
        for col in mat_cols_copy:
            count_zero = count_zeros(col)
            if(count_zero > max_zeros and exist_0_non_convered(col)):
                max_zeros = count_zero
                toCover = col
                row_col_i = ["col", ci]
            ci += 1
        
        for t in toCover:
            t.set_cover()

        if(len(row_col_i) > 0):
            len_coveres += 1

            if(row_col_i[0] == "row"):
                mat_rows_copy.pop(row_col_i[1])
            elif(row_col_i[0] == "col"):
                mat_cols_copy.pop(row_col_i[1])

    return len_coveres
       
# Create additional zeros
def step4():
    min_global = min_all()

    for row in matrix_rows:
        indice = 0

        for e in row:
            if(e.isCovered()):
                if(e.get_covered() > 1):
                    row[indice].setValue(e.getValue() + min_global)
            else:
                row[indice].setValue(e.getValue() - min_global)

            indice += 1

def Hungrian():
    len_coveres = 0

    step1()
    print_matrix()

    step2()
    print_matrix()
    
    while True:
        len_coveres = step3(len_coveres)
        print_matrix()

        if(len_coveres >= len(matrix_rows)):
            break

        step4()
        print_matrix()

    
Hungrian()
