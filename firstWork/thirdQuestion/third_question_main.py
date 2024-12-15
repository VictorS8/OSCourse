import threading
import time
import random

# Questão 3: [1 ponto]
#  No problema dos leitores e escritores, realize uma simulação para comparar duas soluções.
#   Na primeira, os escritores são obrigados a esperar para acessar a região crítica sempre que houver
#  leitores, fato que pode levar os escritores a esperar indefinidamente pelo acesso.
#   Na segunda, essa possibilidade de espera indefinida dos escritores é resolvida.
#  Discuta os achados.
#       Leitura recomendada:
#           COURTOIS, Pierre-Jacques; HEYMANS, Frans; PARNAS, David Lorge . Concurrent control with
#           “readers” and “writers”. Communications of the ACM, v. 14, n. 10, p. 667-668, 1971.

numero_de_leitores = 5
numero_de_escritores = 3
tempo_de_simulacao = 10
random.seed(42)

def simular_leitores_escritores(solucao):
    threads = []

    for i in range(numero_de_leitores):
        t = threading.Thread(target=solucao.leitor, args=(i,))
        t.daemon = True
        threads.append(t)

    for i in range(numero_de_escritores):
        t = threading.Thread(target=solucao.escritor, args=(i,))
        t.daemon = True
        threads.append(t)

    for t in threads:
        t.start()

    time.sleep(tempo_de_simulacao)
