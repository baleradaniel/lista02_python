# 04 - Faça um programa que calcule um aumento de 15% para um salário de R$750



salario = float(input('Digite o salario: '))
aumento = float(input('Digite a porcentagem de aumento: '))
novo_salario = salario + (salario * aumento/100)
print('Novo salario: ',novo_salario)