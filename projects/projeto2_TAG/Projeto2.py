# Projeto 2 da disiciplina de Teoria e Aplicação de Grafos - TAG, Universidade de Brasília - UnB.
# Desenvolvido por Oseias Romeiro Magalhães - 211036123

from Professor import Professor
from Escola import Escola

# abre o arquivo para leitura
file = open('./entrada.txt')

# dados
professores = []
escolas = []

## coleta os dados do arquivo
lerEscolas = False # faz a troca para leitura de escolas
for f in file:

    if(f[0] != '/' and f[0] != '\n' and f[0] != ''):

        if(lerEscolas): # escolas
            escola = ""
            for char in f:
                if(char not in ['(',')','\n']):
                    escola += char
            escola = escola.replace(':', ' ').split(' ')
            
            codigo = escola.pop(0)
            habilitacoes = []
            for e in escola:
                habilitacoes.append(int(e))

            # codigo: str , habalitações: list
            escolas.append(Escola(codigo, habilitacoes))

        else: # professores
            professor = ""
            for char in f:
                if(char not in [',',':','(',')','\n']):
                    professor += char
            professor = professor.split(' ')
            
            codigo = professor.pop(0)
            habilitacoes = professor.pop(0)

            # codigo: str, habalitações: str, escolas: list
            professores.append(Professor(codigo, int(habilitacoes), professor))
        
    if(f == '//\n'):
        lerEscolas = True


# fecha o arquivo
file.close()

## Gale-Shapley

# escola e professores ja foram instanciados como livres
resultado = {}# dicionario com o resultado (chaves são os código das escolas)
prof_i = 0
while len(resultado) < len(escolas):

    # pega o professor
    professor = professores[prof_i]

    if(len(professor.escolas) > 0 and professor.livre()):

        # pega a 1º escola das preferencias do professor que ele ainda não a ofertou
        prox_escola = professor.prox()
        for e in escolas:
            if(e.codigo == prox_escola):
                escola_preferida = e
                break
        
        # a escola esta livre
        if(not escola_preferida.preenchido()):

            # professor é aceito
            escola_preferida.aceita(professor)
            if(escola_preferida.codigo in resultado.keys()):
                resultado[escola_preferida.codigo].append(professor.codigo)
            else:
                resultado[escola_preferida.codigo] = [professor.codigo]

        else:
            # verifica se esse novo professor satisfaz mais a escola ou se o professor tem maior prioridade
            c = 0 # cargo
            for prof_aceito in escola_preferida.professores:
                if(
                    # professor satisfaz a escola
                    professor.habilitacoes >= escola_preferida.habilitacoes[c]
                    and
                    (
                        # professor_aceito nao satisfaz a escola
                        prof_aceito.habilitacoes < escola_preferida.habilitacoes[c]
                        or
                        # professor tem mais preferencia que o professor_aceito
                        professor.preferencia(escola_preferida.codigo) < prof_aceito.preferencia(escola_preferida.codigo)
                        or
                        (
                            # professor se encaixa melhor nos requisitos da escola
                            (professor.habilitacoes / escola_preferida.habilitacoes[c] < prof_aceito.habilitacoes / escola_preferida.habilitacoes[c])
                            and
                            # professor tem mais ou igual preferencia (preferencia é medida pela posição da escola na lista de preferencia)
                            professor.preferencia(escola_preferida.codigo) <= prof_aceito.preferencia(escola_preferida.codigo)
                        )
                    )
                ):

                    # cancela a aprovação do professor
                    prof_removido = escola_preferida.cancela(c)
                    resultado[escola_preferida.codigo].remove(prof_removido.codigo)

                    # aceita esse novo professor
                    escola_preferida.aceita(professor)
                    resultado[escola_preferida.codigo].append(professor.codigo)

                    break
                c += 1
            
    elif(len(professor.escolas) == 0):
        # adiciona todas as escolas ao professor que não é aceito em nenhuma escola de sua preferencia
        for e in escolas:
            professor.escolas.append(e.codigo)

    # proximo professor
    prof_i += 1
    # volta para o primeiro professor
    if(prof_i == len(professores)):
        prof_i = 0

# saida
for r in resultado:
    print(r, ':', resultado[r])

print('\nEscolas preenchidas: ', len(resultado))

# conta os professores
t = 0
for r in resultado.keys():
    t += len(resultado[r])

print('\nProfessores alocados estavelmente: ', t)
