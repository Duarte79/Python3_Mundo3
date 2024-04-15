'''num = [2, 5, 9, 1]
num[2] = 3
print(num)'''

'''num = [2, 5, 9, 1]
num.append(7)
print(num)'''

num = [2, 5, 9, 1]
num.sort()
print(num)

num = [2, 5, 9, 1]
num.sort(reverse=True)
print(num)

num = [2, 5, 9, 1]
num.sort(reverse=True)
print(f'Essa lista tem {len(num)} elementos')

num = [2, 25, 9, 1, 3]
num.insert(2, 0)
print(num)

num = [2, 25, 9, 1, 3]
num.pop()
print(num)

num = [2, 25, 9, 1, 3]
num.pop(3)
print(num)

num = [2, 25, 9, 1, 3]
num.remove(25)
print(num)

num = [2, 25, 9, 1, 3]
if 25 in num:
    num.remove(25)
    print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')

