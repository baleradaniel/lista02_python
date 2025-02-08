# 10 Escreva um programa que pergunte quantos pedaços o bolo tem, em seguida pergunte ao usuario quantos
# pedaços ele comeu, calcule quantos pedaços ainda tem e exiba o resultado com uma mensagem de livre escolha.

bolo_pedacos = int(input('Quantos pedaços tem o bolo? '))
pedacos_comidos = int(input('Quantos pedaços você comeu? '))

print('O bolo contém:', bolo_pedacos)
print('Você comeu:', pedacos_comidos)
print('Sobrou', (bolo_pedacos - pedacos_comidos), 'pedaços de bolo')