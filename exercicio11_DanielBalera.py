#11 Escreva um programa que pergunte o nome do aniversariante, em seguida pergunte a sua idade, acrescente mais 1 e exiba:
# o nome do aniversariante seguida da mensagem "no proximo aniversario você terá" idade , "anos".

nome = input('Escreva o nome do aniversariante: ')
idade = int(input('Insira a idade: '))

print(nome, 'no proximo aniversario você terá', idade + 1, "anos.")