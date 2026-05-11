"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz') # __iter__()

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto
#   print(letra)
texto = 'Luiz' # iterável
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        print('Acabou a iteração')
        break