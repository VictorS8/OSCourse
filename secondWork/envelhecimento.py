def envelhecimento(paginas, capacidade):
    molduras_na_memoria = []
    contadores = {}
    faltas_de_memoria = 0

    for pagina in paginas:
        if pagina in molduras_na_memoria:
            contadores[pagina] = (contadores[pagina] >> 1) | (1 << 7)

        if pagina not in molduras_na_memoria:
            faltas_de_memoria += 1
            if len(molduras_na_memoria) == capacidade:
                pagina_substituir = min(molduras_na_memoria, key=lambda p: contadores[p])
                molduras_na_memoria.remove(pagina_substituir)
                del contadores[pagina_substituir]

            molduras_na_memoria.append(pagina)
            contadores[pagina] = 1 << 7

        print('------------------------')
        print(f"Página {pagina}: Memória -> {molduras_na_memoria}")
        print(f"Contadores: {contadores}\n")
        for processo, contador in contadores.items():
            print(f"Processo {processo}: Contador = {contador:08b}")

        for processo in molduras_na_memoria:
            contadores[processo] = contadores[processo] >> 1

    return faltas_de_memoria