
class Person:
    def __init__(self, name: str, attracted: list = []) -> None:
        self.attracted = attracted
        self.choosed: Person = None
        self.name = name
    
    def __str__(self) -> str:
        return self.name

m1 = Person('1')
m2 = Person('2')
m3 = Person('3')
m4 = Person('4')
m5 = Person('5')

MEN = [m1, m2, m3, m4, m5]

w1 = Person('A', [m3, m5, m2, m1, m4])
w2 = Person('B', [m5, m2, m1, m4, m3])
w3 = Person('C', [m4, m3, m5, m1, m2])
w4 = Person('D', [m1, m2, m3, m4, m5])
w5 = Person('E', [m2, m3, m4, m1, m5])

WOMEN = [w1, w2, w3, w4, w5]

m1.attracted = [w3, w2, w5, w1, w4]
m2.attracted = [w1, w2, w5, w3, w4]
m3.attracted = [w2, w3, w2, w1, w5]
m4.attracted = [w1, w3, w4, w2, w5]
m5.attracted = [w1, w2, w3, w5, w3]

# return if exist a man single
def existMsingle() -> bool:
    for m in MEN:
        if(m.choosed == None):
            return True
    return False

# return the position of person choosed in attractedd list
def pos(person: Person, p_choose) -> int:
    i = 0
    if(p_choose == None):
        return 9999 # accept the other

    for d in person.attracted:
        if(d == p_choose):
            return i
        else:
            i += 1

c = 0
i = 0
rem = False
while existMsingle():
    # choose m in MEN list
    m = MEN[i]

    # choose women in attractedd list in
    w: Person = None
    for wattractedd in m.attracted:
        if(wattractedd != m.choosed):
            w = wattractedd
            break
    
    if(w != None):
        if(w.choosed == None):

            # break with the current
            if(m.choosed != None):
                w_current = m.choosed
                w_current.choosed = None

            # new relationship
            m.choosed = w
            w.choosed = m

        elif(pos(w, m) < pos(w, w.choosed) and pos(m, w) < pos(m, m.choosed)):

            # break with the current
            if(m.choosed != None):
                w_current = m.choosed
                w_current.choosed = None
            m_current = w.choosed
            m_current.choosed = None

            # new relationship
            m.choosed = w
            w.choosed = m
        
        else:
            # active the removal
            if(c > 0 and i == 0):
                if(rem):
                    rem = False
                else:
                    rem = True
            
            # forget her
            if(rem):
                m.attracted.remove(w)
        
    i += 1
    c += 1
    if(i == len(MEN)):
        i = 0

print('\nMEN:')
for m in MEN:
    print(m, m.choosed)

print('\nWOMEN:')

for w in WOMEN:
    print(w, w.choosed)

print(f'\nInteractions: {c}')
