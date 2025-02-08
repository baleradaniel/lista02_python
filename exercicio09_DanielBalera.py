# 09 Escreva um programa que peça ao usuário para inserir três números inteiro, some os dois primeiros e multiplique esse total pelo terceiro. 
# Exiba o resultado da operação com a seguinte mensagem: "O total é: [?]".

n1 = int(input('Insira numero 1: '))
n2 = int(input('Insira numero 2: '))
n3 = int(input('Insira numero 3: '))
soma = n1 + n2
resultado = soma * n3
print('O total é:', resultado)