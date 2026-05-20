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

lista = [10, 20, 30, 40]
lista.append('Lucas')
lista.append(1533)
del lista[-1]
# lista.clear()
lista.insert(0, 5) # 1° Valor é o indice onde quero adicionar e o 2° é o valor que quero adicionar
print(lista)