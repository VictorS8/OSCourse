def fifo(paginas, capacidade):
    molduras_na_memoria = []
    faltas_de_memoria = 0

    for pagina in paginas:
        if pagina not in molduras_na_memoria:
            faltas_de_memoria += 1
            if len(molduras_na_memoria) == capacidade:
                molduras_na_memoria.pop(0)
            molduras_na_memoria.append(pagina)

        print(f'Página {pagina}: Memória -> {molduras_na_memoria}')
        print(f'Falta de memoria em cada iteração: {faltas_de_memoria}')

    return faltas_de_memoria