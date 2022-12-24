class Queue:
    def __init__(self, li:list):
        self.l = li

    def Get(self):
        return self.l.pop(0)

    def Add(self, e) -> None:
        self.l.append(e)

    def isEmty(self) -> bool:
        return len(self.l) == 0

# graph bipartite
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'G', 'H'],
    'C': ['H', 'D'],
    'D': ['C', 'I'],
    'E': ['F', 'I'],
    'F': ['A', 'E', 'G'],
    'G': ['F', 'B'],
    'H': ['B', 'C', 'I'],
    'I': ['D', 'E', 'H'],
}
# not bipartite
adjacency_list2 = {
    'A': ['B', 'F'],
    'B': ['A', 'H'],
    'C': ['H', 'D'],
    'D': ['C', 'I'],
    'E': ['F', 'I'],
    'F': ['A', 'E', 'G'],
    'G': ['F', 'H'],
    'H': ['B', 'C', 'H', 'I'],
    'I': ['D', 'E', 'H'],
}
# initial vertex
init = 'A'

# sets
V1 = [init]
V2 = []

# vertex has already checked 
marked = [init]

# init queue
queue = Queue([init])

while not queue.isEmty():
    v = queue.Get()
    for neighbor in adjacency_list[v]:
        if(neighbor in marked):
            if((v in V1 and neighbor in V1) or (v in V2 and neighbor in V2)):
                raise Exception('Error: this graph in not bipartite!')
        else:
            marked.append(neighbor)
            queue.Add(neighbor)
            if(v in V1):
                V2.append(neighbor)
            elif(v in V2):
                V1.append(neighbor)

print('Set A:', V1)
print('Set B:', V2)
