"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta os espaços no começo e no fim da frase
rstrip - corta os espaços da direita
lstrip - corta os da esquerda
"""

frase = 'Olha só que,      coisa interessante'
lista_palavras_cruas = frase.split(',')

lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())

# print(lista_palavras)
# print(lista_palavras_cruas)
frases_unidas = ', '.join(lista_palavras)
print(frases_unidas)