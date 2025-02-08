# Escreva um programa que solicite um determinado numero de dias, em seguida exiba o quanto esses dias equivalem em horas, minutos e segundos

n_dias = int(input('Insira a quantidade de dias: '))
n_horas = n_dias*24
n_minutos = n_horas*60
n_segundos = n_minutos*60

print(n_dias, "dias equivalente em horas são", n_horas)
print(n_dias, "dias equivalente em minutos são", n_minutos)
print(n_dias, "dias equivalente em segundos são", n_segundos)