"""
Exercicio
Exiba os índices da lista
0 Maria 
1 Helena 
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Lucas')


i = range(len(lista))

for indice in i:
    print(indice, lista[indice])
    