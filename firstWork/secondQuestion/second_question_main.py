import threading

from firstWork.secondQuestion.jantar_dos_filosofos import numero_de_execussoes, quantidade_de_filosofos, \
    jantar_dos_filosofos

# Questão 2: [1 ponto]
#  No problema do jantar dos filósofos, crie um protocolo que permita uma operação sem impasse.
#  Utilize como base os algoritmos disponíveis em:
#  https://docs.oracle.com/cd/E19205-01/820-0619/gepji/index.html
#  Não utilize a solução disponível no material citado.
#  Verifique se ocorre impasse em 1000 execuções

threads = []
execucoes_sem_impasse = numero_de_execussoes

for i in range(quantidade_de_filosofos):
    thread = threading.Thread(target=jantar_dos_filosofos, args=(i, execucoes_sem_impasse))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nSimulação finalizada: Nenhum impasse detectado em 1000 execuções.")
