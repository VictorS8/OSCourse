"""
Questão 1: [2 pontos]

Escreva um programa que compare um sistema de paginação usando o algoritmo FIFO com o algoritmo de envelhecimento.

O número de molduras de páginas é um parâmetro. A sequência de referências de páginas deve ser organizada simulando
    conjuntos de trabalho de processos. Cada conjunto de trabalho deve representar o comportamento típico de acesso
    a páginas de memória de um processo e pode variar em tamanho e duração.

Simule diferentes processos com tamanho e duração de conjuntos de trabalho distintos e anote as sequências
    de referências geradas em um arquivo para conferência. Para cada um dos processos simulados, analise o número
    de faltas de página por 1000 referências de memória como função do número de molduras de páginas disponíveis.
"""
from secondWork.gerar_lista_grande_com_tendencia import gerar_lista_grande
from collections import Counter

"""
FIFO (First-In, First-Out)
Funcionamento:
As páginas são organizadas em uma fila na ordem em que foram carregadas na memória. Quando é necessário substituir 
    uma página (por falta de espaço), a página que está há mais tempo na memória (a primeira da fila) é removida.
    
Vantagem: Simples de implementar.
Desvantagem: Pode causar a anomalia de Belady, onde mais quadros podem levar a mais falhas de página.

Envelhecimento
Funcionamento:
Cada página recebe um contador que reflete sua frequência de uso recente. Periodicamente, os contadores de todas 
    as páginas são deslocados para a direita (envelhecem), e um bit adicional é adicionado para indicar se a página 
    foi acessada no último período. Quando é necessário substituir uma página, a página com o menor valor no 
    contador (menos usada recentemente) é escolhida.
    
Vantagem: Considera o histórico de uso das páginas, oferecendo melhor desempenho em geral.
Desvantagem: Mais complexo de implementar e consome mais recursos computacionais.
"""

# TODO: Comparar número de molduras de páginas entre os 2 algoritmos

# TODO: Conseguir criar um Conjunto de trabalho gigante de processos com diferentes comportamentos típicos onde
#   se repete algum tipo de padrão como: A, B, C, E, F, A, B, D, H, B, C, A, porem em uma escala muito maior.
#   E principalmente guardar esse conjunto de trabalho de processos usados para cada iteração de comparação entre os
#   algoritmos

# TODO: Parâmetros que serão mudados para comparação do projeto no trabalho 2
#   1 - Numero de molduras de páginas
#   2 - Conjunto de trabalho de processos com comportamento típico (Guardar tamanho e duração de cada processo,
#   e sequência dos processos)
#   3 - Variar entrar algoritmo FIFO e Envelhecimento

numero_de_molduras = 15

lista_base_do_conjunto_de_trabalho = ["I/O 1", "I/O 2", "Checking File 1", "I/O 3", "Checking File 2"]
frequencia_de_tendencia = [0.3, 0.2, 0.3, 0.1, 0.1]
tamanho_do_conjunto_de_trabalho = 3000

conjunto_de_trabalho = gerar_lista_grande(lista_pequena= lista_base_do_conjunto_de_trabalho,
                                          proporcoes= frequencia_de_tendencia,
                                          tamanho= tamanho_do_conjunto_de_trabalho)

lista_de_tendencia_do_conjunto_de_trabalho = Counter(conjunto_de_trabalho)

print(conjunto_de_trabalho)

with open(file= 'info.txt', mode= 'w') as file:
    file.write('- Information about Working Set -\n\n')

with open(file= 'info.txt', mode= 'a') as file:
    file.write(f'Working Set length: {len(conjunto_de_trabalho)}\n')
    file.write(f'Base Working Set: {lista_base_do_conjunto_de_trabalho}\n')
    file.write(f'Proportion of the Working Set: {frequencia_de_tendencia}\n')
    file.write(f'Trend List of the Working Set: {lista_de_tendencia_do_conjunto_de_trabalho}\n')
