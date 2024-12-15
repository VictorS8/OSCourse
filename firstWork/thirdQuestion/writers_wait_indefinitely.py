import threading
import time
import random

from firstWork.thirdQuestion.third_question_main import simular_leitores_escritores

class LeitoresEscritoresEsperaIndefinida:
    def __init__(self):
        self.mutex = threading.Lock()
        self.reader_count = 0
        self.resource = threading.Lock()

    def leitor(self, id_leitor):
        while True:
            time.sleep(random.uniform(0.5, 2))
            with self.mutex:
                self.reader_count += 1
                if self.reader_count == 1:
                    self.resource.acquire()
            print(f"Leitor {id_leitor} está lendo...")
            contador_acessos["leitores"] += 1
            time.sleep(random.uniform(0.5, 1))
            with self.mutex:
                self.reader_count -= 1
                if self.reader_count == 0:
                    self.resource.release()

    def escritor(self, id_escritor):
        while True:
            time.sleep(random.uniform(1, 3))
            with self.resource:
                print(f"Escritor {id_escritor} está escrevendo...")
                contador_acessos["escritores"] += 1
                time.sleep(random.uniform(0.5, 1))

print("=== Solução 1: Escritores podem esperar indefinidamente ===")
solucao_espera_indefinida = LeitoresEscritoresEsperaIndefinida()
contador_acessos = {"leitores": 0, "escritores": 0}
simular_leitores_escritores(solucao_espera_indefinida)
print("Acessos (Solução 1):", contador_acessos)