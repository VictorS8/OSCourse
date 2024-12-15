import numpy as np
import matplotlib.pyplot as plt

from firstWork.firstQuestion.round_robin import round_robin_com_metricas

# Questão 1: [1 ponto]
#  Crie uma simulação utilizando o algoritmo de escalonamento Round Robin. Dado N processos com
#  diferentes burst time, analise as métricas tempo médio de espera, tempo médio de retorno e vazão
#  para diferentes valores de quantum.
#   Considere:
#   • Todos os N processos tem o mesmo tempo de chegada.
#   • 1 unidade de tempo é gasto para a mudança de contexto do processo.
#   • Tempo médio de espera (+/−std): Tempo médio que um processo passa no estado de pronto
#  antes de ser executado.
#   • Tempo médio de retorno (+/ − std): Tempo médio que um processo leva para ser concluído
#  após sua chegada ao sistema.
#   • Vazão: Quantidade de processos concluídos em um determinado período.
#
#  Exiba a sequência de execução de cada processo para os diferentes valores de quantum. Utilize a
#  linguagem de programação de seu interesse.

# Simulação do Algoritmo Round Robin

processos = ["Processo 1", "Processo 2", "Processo 3", "Processo 4"]
burst_times = [1, 4, 25, 35]
lista_de_quantum = [2, 8, 24]

for quantum in lista_de_quantum:
    print(f"\nResultados para o determinado Quantum: {quantum}")
    print()

    (sequencia_de_execucao_do_quantum,
     tempo_medio_de_espera_do_quantum,
     desvio_padrao_do_tempo_de_espera_do_quantum,
     tempo_medio_de_retorno_do_quantum,
     desvio_padrao_do_tempo_de_retorno_do_quantum,
     vazao_do_quantum) = round_robin_com_metricas(quantum, processos, burst_times)

    print(f"Sequência de execução do Quantum: {sequencia_de_execucao_do_quantum}")
    print(f"Tempo médio de espera do Quantum: {tempo_medio_de_espera_do_quantum:.2f} +/- {desvio_padrao_do_tempo_de_espera_do_quantum:.2f}")
    print(f"Tempo médio de retorno do Quantum: {tempo_medio_de_retorno_do_quantum:.2f} +/- {desvio_padrao_do_tempo_de_retorno_do_quantum:.2f}")
    print(f"Vazão do Quantum: {vazao_do_quantum:.2f} processos/unidade de tempo")

    quantum_labels = [str(q) for q in lista_de_quantum]
    tempos_espera_media = [tempo_medio_de_espera_do_quantum for q in lista_de_quantum]
    tempos_retorno_media = [tempo_medio_de_retorno_do_quantum for q in lista_de_quantum]
    vazoes = [vazao_do_quantum for q in lista_de_quantum]

    x = np.arange(len(lista_de_quantum))
    width = 0.4

    # Gráfico 1: Tempo Médio de Espera e Retorno
    plt.figure(figsize=(4, 4))

    plt.bar(x - width / 2, tempos_espera_media, width, label="Tempo Médio de Espera")
    plt.bar(x + width / 2, tempos_retorno_media, width, label="Tempo Médio de Retorno")

    plt.xlabel("Quantum")
    plt.ylabel("Tempo (unidades)")
    plt.title("Tempos Médios de Espera e Retorno para Diferentes Quantum")
    plt.xticks(x, quantum_labels)
    plt.legend()
    plt.grid()

    plt.show()

    # Gráfico 2: Vazão
    plt.figure(figsize=(4, 4))

    plt.bar(quantum_labels, vazoes, color='skyblue')
    plt.xlabel("Quantum")
    plt.ylabel("Vazão (processos/unidade de tempo)")
    plt.title("Vazão para Diferentes Quantum")
    plt.grid()

    plt.show()
