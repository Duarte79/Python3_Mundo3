'''num = [2, 5, 9, 1]
num[2] = 3
print(num)'''

'''num = [2, 5, 9, 1]
num.append(7)
print(num)'''

'''num = [2, 5, 9, 1]
num.sort()
print(num)'''

'''num = [2, 5, 9, 1]
num.sort(reverse=True)
print(num)'''

'''num = [2, 5, 9, 1]
num.sort(reverse=True)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2, 25, 9, 1, 3]
num.insert(2, 0)
print(num)'''

'''num = [2, 25, 9, 1, 3]
num.pop()
print(num)'''

'''num = [2, 25, 9, 1, 3]
num.pop(3)
print(num)'''

'''num = [2, 25, 9, 1, 3]
num.remove(25)
print(num)'''

'''num = [2, 25, 9, 1, 3]
if 25 in num:
    num.remove(25)
    print(num)'''


'''valor = list()
valor.append(5)
valor.append(9)
valor.append(4)
for c, v in enumerate(valor):
    print(f'na posição {c} encontrei o valor {valor}')'''

'''valores = list()
for cont in range(5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')'''

a = [1, 2, 3, 4, 5, 6]
b = a
b[2] = 8

print('lisra A', a)
print('lista B', b)

a = [1, 2, 3, 4, 5, 6]
b = a[:]
b[2] = 8
print('lista A', a)
print('lista B', b)

