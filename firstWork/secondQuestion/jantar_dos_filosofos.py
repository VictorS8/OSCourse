import threading
import time
import random

quantidade_de_filosofos = 5
numero_de_execussoes = 1000

garfos = [threading.Lock() for _ in range(quantidade_de_filosofos)]

def jantar_dos_filosofos(filosofo_id, execucoes_sem_impasse):
    for _ in range(execucoes_sem_impasse):
        print(f"Execussao {_}")
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Filósofo {filosofo_id} está pensando.")

        garfo_esquerdo = filosofo_id
        garfo_direito = (filosofo_id + 1) % quantidade_de_filosofos

        primeiro, segundo = sorted([garfo_esquerdo, garfo_direito])

        with garfos[primeiro]:
            with garfos[segundo]:
                print(f"Filósofo {filosofo_id} está comendo.")
                time.sleep(random.uniform(0.1, 0.3))

        print(f"Filósofo {filosofo_id} terminou de comer.")