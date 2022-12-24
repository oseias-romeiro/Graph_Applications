from random import randint, shuffle

class Sudoku:
    def __init__(self):
        self.ordem: int = 9 # quadrado maior
        self.ordem_section: int = 3 # quadrado menor
        self.base_color:int = 0
        self.sudoku_matrix: dict = dict()
        self.solutions = []
        self.colors = list(range(1, self.ordem+1))


        self.init_sudoku()

    # traduz o indice do vertice para coordenadas x,y    
    def get_cord(self, ele_indice):
        quot = ele_indice//self.ordem
        rest = ele_indice%self.ordem

        if rest != 0:
            x = quot + 1
            y = rest
        else:
            x = quot
            y = self.ordem

        return x, y

    # verifica dois vertices se estão no mesmo bloco
    def section_eq(self, a, b, sections):

        pos_a = self.get_cord(a)
        pos_b = self.get_cord(b)

        for s in sections:
            if (pos_a[0] in s[0]) and (pos_a[1] in s[1]):
                section_a = s

            if (pos_b[0] in s[0]) and (pos_b[1] in s[1]):
                section_b = s
            

        return section_a == section_b

    # verifica se 2 elementos estão na mesma direção: linha/coluna
    def in_same_direction(self, a , b):
        cord_a = self.get_cord(a)
        cord_b = self.get_cord(b)
        
        return (cord_a[0] == cord_b[0] or cord_a[1] == cord_b[1])
        
    # define os vertices vizinhos e a coloração incial
    def init_neighbors_colors(self, matrix: dict):
        if "N" in matrix[list(matrix.keys())[0]]:
            return {n: {"N": matrix[n]["N"], "color": self.base_color} for n in matrix.keys()}

        else:
            return {n: {"N": matrix[n], "color": self.base_color} for n in matrix.keys()}
       
    # define "lock", para que o usuário não mude os items gerados no sudoku
    def lock_items(self):
        matrix = {}
        for n in self.sudoku_matrix.keys():
            matrix[n] = {"N": self.sudoku_matrix[n]["N"], "color": self.sudoku_matrix[n]["color"], "lock": self.sudoku_matrix[n]["color"] != self.base_color}

        self.sudoku_matrix = matrix
        
    # inicializa o sudoku vazio
    def init_sudoku(self) -> None:

        matrix = {x: set() for x in range(1, (self.ordem**2)+1)}

        # formato de um bloco
        sections = [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [7, 8, 9]], [[4, 5, 6], [1, 2, 3]], [[4, 5, 6], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]], [[7, 8, 9], [1, 2, 3]], [[7, 8, 9], [4, 5, 6]], [[7, 8, 9], [7, 8, 9]]]

        for a in matrix.keys():
            for b in matrix.keys():
                if (a != b) and (self.section_eq(a, b, sections) or self.in_same_direction(a, b)):
                    matrix[a].add(b)

        self.sudoku_matrix = self.init_neighbors_colors(matrix)
        
        self.lock_items()

    # verifica se a cor já nao está sendo usada entre os adjacentes
    def is_Valid(self, graph, v, color):
        for n in graph[v]["N"]:
            if color == graph[n]["color"]:
                return False

        return True

    # apaga elementos aleatorios
    def erase_elem(self):
        rand_elem = randint(1, len(self.sudoku_matrix.keys()))

        while self.sudoku_matrix[rand_elem]["color"] == 0:
            rand_elem = randint(1, len(self.sudoku_matrix.keys()))

        self.sudoku_matrix[rand_elem]["color"] = 0
        self.lock_items()
        self.solutions = []
        
    # coloração sem backtracking
    def graphColoring(self, graph: dict, colors, vertex):
        if vertex == len(graph.keys())+1:
            self.sudoku_matrix = graph
            return True

        shuffle(colors)
        for c in colors:
            if self.is_Valid(graph, vertex, c):
                graph[vertex]["color"] = c

                if self.graphColoring(graph, colors, vertex+1):
                    return True

                graph[vertex]["color"] = 0

        return False

    # Algoritmo de coloração com backtracking
    def graphColoring_back(self, graph, colors, vertex):
        
        if vertex == len(graph.keys())+1:
            self.solutions.append({v: graph[v]["color"] for v in graph.keys()})
            
            if (len(self.solutions) == 1):
                print("Solução encontrada.")

            return

        if not graph[vertex]["lock"]:
            if (len(self.solutions) == 0):
                print("# Vertice: " + str(vertex))
            
            for c in colors:
                if self.is_Valid(graph, vertex, c):
                    
                    if (len(self.solutions) == 0):
                        print(str(c) + " esta disponivel")
                        
                    graph[vertex]["color"] = c
                    
                    self.graphColoring_back(graph, colors, vertex+1)

                    graph[vertex]["color"] = 0
                else:
                    if (len(self.solutions) == 0):
                        print(str(c) + " não esta disponivel")
        else:
            self.graphColoring_back(graph, colors, vertex+1)
        
    def gen_complete(self):
        matrix_init = self.init_neighbors_colors(self.sudoku_matrix)
        
        self.graphColoring(matrix_init, self.colors, 1)
        self.lock_items()
        
    # gera um sudoku completo e remove o maximo elementos de forma que tenha apenas uma solução
    def generator(self):
        self.gen_complete()
        
        self.erase_elem()
        self.graphColoring_back(self.sudoku_matrix, self.colors, 1)
        
        while len(self.solutions) == 1:
            last_graph = {v: self.sudoku_matrix[v]["color"] for v in self.sudoku_matrix.keys()}
            self.erase_elem()
            self.graphColoring_back(self.sudoku_matrix, self.colors, 1)

        for i in last_graph.keys():
            self.sudoku_matrix[i]["color"] = last_graph[i]
        
        self.lock_items()
        self.solutions = []