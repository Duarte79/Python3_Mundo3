'''lanche = ('Hamburguer', 'suco', 'Pizza', 'pudim')
print('A', lanche[-2])
print('B', lanche[1:3])
print('C', lanche[2:])
print('D', lanche[:2])
print('E', lanche[-2:])
print('F', lanche[3:])
print(lanche)'''
#tuplas são imutáveis

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
print(len(lanche))
print('Comi pra caramba!')

'''0: Hamburguer
1: Suco
2: Pizza
3: Pudim

Agora, quando você faz algo como lanche[1:3], está basicamente dizendo “me dê os lanches da posição 1 até a posição 3, mas não inclua o lanche na posição 3”. Então, você obtém ‘Suco’ e ‘Pizza’.

Quando você faz lanche[2:], está dizendo “me dê todos os lanches a partir da posição 2”. Então, você obtém ‘Pizza’ e ‘Pudim’.

Quando você faz lanche[:2], está dizendo “me dê todos os lanches até a posição 2, mas não inclua o lanche na posição 2”. Então, você obtém ‘Hamburguer’ e ‘Suco’.

Quando você faz lanche[-2:], está dizendo “me dê os últimos dois lanches”. Então, você obtém ‘Pizza’ e ‘Pudim’.

Espero que isso ajude a entender melhor o código! Se você tiver mais perguntas, fique à vontade para perguntar.'''