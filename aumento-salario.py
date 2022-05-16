salario = float(input('Qual é o salário do funcionário? R$'))
salario2 = salario + salario * 15 / 100
print(('O funcionário que ganhava R${}, com 15% de aumento vai ganhar RS{:.2f}'.format(salario, salario2)))