# Bron-Kerbosch

## Projeto 1 de Teoria e Aplicação de Grafos

Neste projeto foi desenvolvido o algoritmo de Bron-Kerbosch com pivotemento e sem pivotemento. Algoritmo na qual faz a busca de cliques maximais em um grafo (clique que não pode ser expandido, ou seja, não é subconjunto de um clique maior).
Além disso, também é calculado o Coeficiente de Algomeração do grafo, que é a média de algomeração dos nós do grafo.

## Projeto

### Entrada e tratamento de dados
O funcionamento desse programa se dar pelo consumo dos dados do arquivo [soc-dolphins.mtx](./soc-dolphins.mtx) que após ser tratados são instanciados usando a classe [Node](./Node.py) que contém os atributos `name` com o nome do nó e `neighbors`, uma lista contendo os nós vizinhos istanciados, e junto é calculado o Coeficiente de Algomeração.

### Algoritmo
Depois, esses dados são utilizados nos [algoritmos Bron-Kerbosch](./BKalgorithms.py) para fazer a busca de maximais.

### Saída
Todos esses arquivos são utilizados pelo arquivo princial [BKmain](BKmain.py), que deve ser executado, contendo 3 saidas:
- lista de maixmais usando o algoritmo de Bron-Kerbosch sem pivoteamento
- lista de maixmais usando o algoritmo de Bron-Kerbosch com pivoteamento
- Coeficiente de Algomeração do grafo

## Executando

Abra o terminal e entre no diretório do projeto `BRON-KERBOSCH` e execute o comando:

```cmd
    py BKmain.py
```

## Fim

Este projeto foi construido partindo do algoritmo implementado em [Using Bron Kerbosch algorithm to find maximal cliques in O(3^(N/3))](https://iq.opengenus.org/bron-kerbosch-algorithm/ "iq.opengenus.org").
