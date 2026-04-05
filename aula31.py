"""
Flag (Banceira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None

if condicao:
  print('Faça algo')
  passou_no_if = True
else:
  print('Não faça algo')

if passou_no_if is None:
  print('Não passou no if')
else:
  print('Passou no if')