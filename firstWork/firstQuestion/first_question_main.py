import numpy as np

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
burst_times = [10, 5, 8, 6]
lista_de_quantum = [4, 6]

numero_de_processos = len(processos)
burst_restante = burst_times.copy()
tempos_de_espera = [0] * numero_de_processos
tempos_de_retorno = [0] * numero_de_processos
sequencia_de_execucao = []

def round_robin_com_metricas(each_quantum):
    tempo = 0

    while any(burst_restante):
        for i in range(numero_de_processos):
            if burst_restante[i] > 0:
                sequencia_de_execucao.append(processos[i])
                tempo_de_execucao = min(each_quantum, burst_restante[i])
                tempo += tempo_de_execucao
                burst_restante[i] -= tempo_de_execucao

                for j in range(numero_de_processos):
                    if j != i and burst_restante[j] > 0:
                        tempos_de_espera[j] += tempo_de_execucao

                if burst_restante[i] == 0:
                    tempos_de_retorno[i] = tempo

                tempo += 1

    tempo_medio_de_espera = np.mean(tempos_de_espera)
    desvio_padrao_do_tempo_de_espera = np.std(tempos_de_espera)
    tempo_medio_de_retorno = np.mean(tempos_de_retorno)
    desvio_padrao_do_tempo_de_retorno = np.std(tempos_de_retorno)
    vazao = numero_de_processos / tempo

    return (sequencia_de_execucao,
            tempo_medio_de_espera,
            desvio_padrao_do_tempo_de_espera,
            tempo_medio_de_retorno,
            desvio_padrao_do_tempo_de_retorno,
            vazao)

for quantum in lista_de_quantum:
    print(f"\nResultados para o determinado Quantum: {quantum}")
    print()

    (sequencia_de_execucao_do_quantum,
     tempo_medio_de_espera_do_quantum,
     desvio_padrao_do_tempo_de_espera_do_quantum,
     tempo_medio_de_retorno_do_quantum,
     desvio_padrao_do_tempo_de_retorno_do_quantum,
     vazao_do_quantum) = round_robin_com_metricas(quantum)

    print(f"Sequência de execução do Quantum: {sequencia_de_execucao_do_quantum}")
    print(f"Tempo médio de espera do Quantum: {tempo_medio_de_espera_do_quantum:.2f} +/- {desvio_padrao_do_tempo_de_espera_do_quantum:.2f}")
    print(f"Tempo médio de retorno do Quantum: {tempo_medio_de_retorno_do_quantum:.2f} +/- {desvio_padrao_do_tempo_de_retorno_do_quantum:.2f}")
    print(f"Vazão do Quantum: {vazao_do_quantum:.2f} processos/unidade de tempo")
