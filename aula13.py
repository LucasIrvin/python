nome = 'Lucas Irvin'
altura = 1.84
peso = 85
imc = peso / altura ** 2

# f-strings significa formatação
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# Lucas Irvin tem 1.84 de altura,
# pesa 85 quilos e seu IMC é
# 25.10633270321361