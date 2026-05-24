"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
Lista só é interessante trabalhar no final dela para que o programa não pese
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6] 
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_c)
print(lista_a)