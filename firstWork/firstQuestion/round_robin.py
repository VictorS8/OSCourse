import numpy as np

def round_robin_com_metricas(cada_quantum, lista_de_processos, burst_times):
    numero_de_processos = len(lista_de_processos)
    burst_restante = burst_times.copy()
    tempos_de_espera = [0] * numero_de_processos
    tempos_de_retorno = [0] * numero_de_processos
    sequencia_de_execucao = []

    tempo = 0

    while any(burst_restante):
        for i in range(numero_de_processos):
            if burst_restante[i] > 0:
                sequencia_de_execucao.append(lista_de_processos[i])
                tempo_de_execucao = min(cada_quantum, burst_restante[i])
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
