import random

def gerar_lista_grande(lista_pequena, proporcoes, tamanho):

    lista_expandida = [
        elemento for elemento, peso in zip(lista_pequena, proporcoes)
        for _ in range(int(peso * 100))
    ]

    lista_grande = [random.choice(lista_expandida) for _ in range(tamanho)]

    return lista_grande

