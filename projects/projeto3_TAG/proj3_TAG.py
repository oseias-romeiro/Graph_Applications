from Tabuleiro import Tabuleiro

menu = """
1 - Jogar
2 - Solução
3 - Sair
"""

# retorna o indice do elemento pelas coordenadas (x,y)
def get_index(control: str):

    try:
        pos, val = control.replace(" ", "").split("=")
        pos_x, pos_y = pos.replace("(", "").replace(")", "").split(",")

        pos_x = int(pos_x)
        pos_y = int(pos_y)
        val = int(val)

        if (val < 0) or (val > 9):
            raise
    except:
        return "# Entrada inválida!"

    matrix_i = ((pos_x-1)*sudoku.ordem) + pos_y

    return [matrix_i, val]


# inicia o jogo
def start():
    print("""### Jogando...\n\n- Digite as entradas no formato: (x,y) = valor\n- Digite 'sair' para desistir (a solução será mostrada)\n- 'check' para verificar sua resposta\n- 'check_input' para ativar/desativar o verificador de entradas\n""")
    while(True):
        control = input()

        if(control == "sair"):
            solution()
            break
        elif(control == "check"):
            if sudoku.valid_solution():
                print("# Parabéns, sua resposta está correta.")
                break
            else:
                print("# Incorreto!\nMas você pode continuar no jogo ou digitar 'sair' para desistir...")
                print(sudoku)

        elif(control == "check_input"):
            if(sudoku.enable_inputChecker):
                print("# input checker desativado!")
            else:
                print("# input checker ativado!")

            sudoku.enable_inputChecker = not sudoku.enable_inputChecker
            
        else:
            fill = get_index(control)

            if isinstance(fill, str):
                print(fill)
            else:
                if sudoku.set_elem(fill[0], fill[1]):
                    print(sudoku)
                

# chama o metodo para solucionar
def solution():
    print("### Solução:\n")
    sudoku.solution()
    print(sudoku)

    input("\nPressione [Enter] para continuar...\n")

    print("------------------ SUDOKU ------------------")


# Core do jogo
print("------------------ SUDOKU ------------------")
cin = ''
while cin != '3':

    # gera proposta para o jogo
    sudoku = Tabuleiro()
    sudoku.generator()
    print(sudoku)

    # entrada
    cin = input(menu) # mostra o menu de controle

    # controle
    if(cin == '1'):
        start()
    elif(cin == '2'):
        solution()
    else:
        pass

print("-------------------- FIM -------------------")
