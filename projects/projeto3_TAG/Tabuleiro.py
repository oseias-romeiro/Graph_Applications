from Sudoku import Sudoku

class Tabuleiro(Sudoku):
    
    def __init__(self):
        super().__init__()
        self.enable_inputChecker = False

    # insere o valor de um elemento
    def set_elem(self, index, value) -> bool:

        if self.sudoku_matrix[index]["lock"]:
            print("# Célula não pode ser alterada!\n")
            return False

        if self.valid_input(index, value):
            self.sudoku_matrix[index]["color"] = value
            print("# Célula preenchida com sucesso.\n")
            return True
        else:
            print("# Alerta: valor inserido é incorreto!\n")
            return False

    # soluciona o sudoku
    def solution(self):
        self.graphColoring_back(self.sudoku_matrix, self.colors, 1)
        
        n_solution = self.solutions[0]
        for i in n_solution.keys():
            self.sudoku_matrix[i]["color"] = n_solution[i]
    
        self.solutions = []
        
        self.lock_items()

    # valida solução
    def valid_solution(self):
        for v in self.sudoku_matrix.keys():
            for n in self.sudoku_matrix[v]["N"]:
                if (self.sudoku_matrix[v]["color"] == 0) or (self.sudoku_matrix[v]["color"] == self.sudoku_matrix[n]["color"]):
                    return False
    
    # valida a entrada se enable_inputChecker for ativado
    def valid_input(self, index, value):

        if(self.enable_inputChecker):
            for n in self.sudoku_matrix[index]["N"]:
                if (self.sudoku_matrix[n]["color"] == value):
                    return False
        return True
    
    # monta o sodoku em string para ser printada na tela
    def __str__(self) -> str:
        sudoku = {v: self.sudoku_matrix[v]["color"] for v in self.sudoku_matrix.keys()}

        sudoku_str = "\n"
        for i in sudoku.keys():
            cord = self.get_cord(i)

            if cord[1] == 1:
                sudoku_str += "| "
            
            sudoku_str += str(sudoku[i])

            if cord[1]%self.ordem != 0:
                sudoku_str += " | "
            else:
                sudoku_str += " |\n"
        
        return sudoku_str