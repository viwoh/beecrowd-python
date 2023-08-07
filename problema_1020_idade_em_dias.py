a = int(input(''))
ano = a // 365
mes = a % 365 // 30
dia = a % 365 % 30

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, mes, dia))