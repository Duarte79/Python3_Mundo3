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

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
print(len(lanche))
print('Comi pra caramba!')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
for cont in range(0, len(lanche)):
    print(cont)'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
for cont in range(0, len(lanche)):
    print(lanche[cont])'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
for cont in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]}')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Fritas')
print(sorted(lanche))'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print('A', c)
print('B', len(c))
print('C', c.count(5))
print('D', c.index(8))