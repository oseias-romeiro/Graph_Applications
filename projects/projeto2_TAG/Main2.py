### 84 emparelhamentos estaveis
import re # utilizado para remover multiplos chars de uma string 
from typing import List
from Professor import Professor
from Escola import Escola

# abre o arquivo para leitura
file = open('./entrada.txt')

# dados
professores: List[Professor] = []
escolas: List[Escola] = []

## coleta os dados do arquivo
lerEscolas = False # faz a troca para leitura de escolas
for f in file:

    if(f[0] != '/' and f[0] != '\n' and f[0] != ''):

        if(lerEscolas): # escolas
            escola = re.sub(r'[()\n]', '', f.replace(':', ' ')).split(' ')
            
            codigo = escola.pop(0)
            habilitacoes = []
            for e in escola:
                habilitacoes.append(int(e))

            # codigo: str , habalitações: list
            escolas.append(Escola(codigo, habilitacoes))

        else: # professores
            professor = re.sub(r'[,:()\n]', '', f).split(' ')
            
            codigo = professor.pop(0)
            habilitacoes = professor.pop(0)

            # codigo: str, habalitações: str, escolas: list
            professores.append(Professor(codigo, int(habilitacoes), professor))
        
    if(f == '//\n'):
        lerEscolas = True


# fecha o arquivo
file.close()

# função determina se o professor satistaz os requisitos da escola
def satisfaz(prof_habili: int, escola_habili: list) -> bool:

    for e in escola_habili:
        if prof_habili >= e:
            return True
    
    return False


prof_escola = {}
prof_i = 0
while len(prof_escola) < len(escolas):

    # pega o primeiro professor
    professor = professores[prof_i]

    if(len(professor.escolas) > 0):

        # pega a escola preferida do professor
        prox = professor.prox()
        for e in escolas:
            if(e.codigo == prox):
                escola_preferida = e
                break

        # habilitações do professor satisfaz a escola?
        if(satisfaz(professor.habilitacoes, escola_preferida.habilitacoes)):

            # a escola ja preencheu todas as vagas?
            if(escola_preferida.preenchido()):
                c = 0
                for prof_aceito in escola_preferida.professores:
                    # verifica se esse novo professor (que satisfaz as habilitações da escola) tem menos habilitaçoes que os professores aceitos
                    if(prof_aceito.habilitacoes not in escola_preferida.habilitacoes and professor.habilitacoes < prof_aceito.habilitacoes):
                        # cancela a aprovação do professor aceito
                        prof_removido = escola_preferida.cancela(c)
                        prof_escola[escola_preferida.codigo].remove(prof_removido.codigo)
                        # aceita esse novo professor
                        escola_preferida.aceita(professor)
                        prof_escola[escola_preferida.codigo].append(professor.codigo)
                        break
                    
                    c += 1
                
            else:
                # escola aceita professor
                escola_preferida.aceita(professor)
                if(escola_preferida.codigo in prof_escola.keys()):
                    prof_escola[escola_preferida.codigo].append(professor.codigo)
                else:
                    prof_escola[escola_preferida.codigo] = [professor.codigo]
        
    else:
        # adiciona todas as escolas ao professor que não é aceito em nenhuma escola de sua preferencia
        for e in escolas:
            professor.escolas.append(e.codigo)

    # proximo professor
    prof_i += 1
    # volta para o primeiro
    if(prof_i == len(professores)):
        prof_i = 0

# saida
print(prof_escola)