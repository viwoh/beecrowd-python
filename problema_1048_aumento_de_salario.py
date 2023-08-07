salario = float(input(''))
if salario > 0 and salario <= 400:
    perc = 15
    reajuste = salario * perc / 100
elif salario <= 800:
    perc = 12
    reajuste = salario * perc / 100
elif salario <= 1200:
    perc = 10
    reajuste = salario * perc / 100
elif salario <= 2000:
    perc = 7
    reajuste = salario * perc / 100
else:
    perc = 4
    reajuste = salario * perc / 100
   

print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(salario + reajuste, reajuste, perc))