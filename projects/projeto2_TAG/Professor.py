
class Professor:

    def __init__(self, codigo: str, habilitacoes: int, escolas: list) -> None:
        self.codigo = codigo
        self.habilitacoes = habilitacoes
        self.escolas = escolas
        self.escolas2 = escolas.copy() # copia para preserva as posições da escola
        self.escola = None
    
    def __str__(self) -> str:
        return self.codigo

    # retorna a 1º escola na lista de preferencias
    def prox(self) -> str:
        return self.escolas.pop(0)
    
    # retorna se o professor esta livre
    def livre(self) -> bool:
        return self.escola == None
    
    # retorna a posição da escola na lista de preferencias (quanto menor = maior preferencia)
    def preferencia(self, esc: str) -> int:
        try :
            return self.escolas2.index(esc)
        except :
            return len(self.escolas2)
        