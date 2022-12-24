# projeto3_TAG

Projeto para uso de algoritmos de coloração de grafos para ser utilizado em solução de partidas do jogo Sudoku.

## Sudoku

O jogo Sudoku clássico propõe uma grade 9x9. Essa grade é dividida em 9 subgrades quadradas 3x3, também chamadas de blocos. O objetivo do jogo é preencher com dígitos de 1 a 9, sendo que nas linhas e colunas dos blocos não pode haver dígitos repetidos.

## Referências

- [M-Coloring Problem](https://www.tutorialspoint.com/M-Coloring-Problem)
- [m Coloring Problem | Backtracking-5](https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/)
- [Coloração de Grafos - Aplicado na resolução do Sudoku](http://ceur-ws.org/Vol-1754/EPoGames_2016_AC_paper_2.pdf)

## Descrição

O projeto é composto de três arquivos:

- [proj3_TAG.py](./proj3_TAG.py): Responsável pelo controle do jogo e é onde está o loop principal que instancia o Sudoku e chama seus métodos, de acordo com a interação com o usuário;
- [Sudoku.py](./Sudoku.py): Contêm a mecânica do jogo sudoku, gera uma proposta de jogo para ser resolvida pelo usuário e também o resolve utilizando algoritmos de coloração de grafos.
- [Tabuleiro.py](./Tabuleiro.py): Contém os métodos responsáveis pela interação com usuário, utilizado no arquivo princial.

# Run
Garanta que os [arquivos necessários](#descrição) estão na mesma path.

```sh
    python3 proj3_TAG.py
```
Ao rodar o programa, deve aparecer menssagens do algoritmo gerando uma sudoku solucionado, apartir dessa solução, o programa removerá elementos do jogo, enquanto ainda existir apenas uma solução. Então apresentará o resultado encontrado mais o menu com a seguinte opções:

1. Jogar: será mostrado instruções de como inserir valores e detalhes de comandos especiais como: `sair`, `check` e `check_input`;
2. Solução: Soluciona o sudoku gerado (esse opção também é acionada ao utilizar o comando 'sair' durante a partida);
3. Sair: fecha o programa.

> Obs.: Pressione qualquer tecla que não faça parte do menu, para gerar um novo sudoku.
