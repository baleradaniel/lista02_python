# Escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem, divida a conta
# pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "cada cliente deve pagar: ", valor

conta = int(input('Qual o valor total da conta? '))
n_clientes = int(input('Quantos clientes existem? '))

valor = conta/ n_clientes

print("cada cliente deve pagar: ", valor)
