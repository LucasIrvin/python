a = 'AAAA'
b = 'B'
c = 1.1

# Erro 'out of range' é porque uma coisa já acabou
# Parametro nomeado é quando dou nome as coisas dentro da chamada das funções

string = 'a={nome2} a={nome2} a={nome2} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)