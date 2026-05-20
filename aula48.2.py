"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
Lista só é interessante trabalhar no final dela para que o programa não pese
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop() # O pop remove o ultimo número da lista nquele momento ou se passado o indice remove o valor que estiver no indice
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)