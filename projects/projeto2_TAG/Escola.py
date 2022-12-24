from Professor import Professor

class Escola:

    def __init__(self, codigo: str, habilitacoes: list) -> None:
        self.codigo = codigo
        self.habilitacoes = habilitacoes
        self.professores = []
    
    # aceita o professor e agora ele nao está mais livre
    def aceita(self, prof: Professor) -> None:
        if(self.preenchido()):
            raise Exception('Erro: time de professores preenchido!')
    
        self.professores.append(prof)
        prof.escola = self
    
    # remove o professor e libera ele
    def cancela(self, prof: int) -> Professor:
        prof_removido = self.professores.pop(prof)
        prof_removido.escola = None
        return prof_removido
    
    # retorna se a escola esta livre (lista de professores < que a quantidade de vagas disponíveis)
    def preenchido(self) -> bool:
        return len(self.professores) >= len(self.habilitacoes)
    
    