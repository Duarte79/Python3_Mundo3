#maior e menor valores na lista
listanum = []
maio = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
       maio = men = listanum[c]
    else:
        if listanum[c] > maio:
           maio = listanum[c]
        if listanum[c] < men:
          men = listanum[c]
print('=-'*30)
print(f'você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maio}, na posição', end=' ')
for i, v in enumerate(listanum):
    if v == maio:
        print(f'{i}...', end=' ')
print(f'O menor valor digitado foi {men} na posição', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}', end='')


