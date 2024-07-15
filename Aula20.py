'''print('_'*30)
print('Curso em vídeo')
print('_'*30)'''

'''def lin():
    print('-'*30)
#Programa principal
lin()
print('Eu sou eu e a minha circustância')
lin()
print('Curso de Python')
lin()
print('teste de função')
lin()'''

'''def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#Programa principal
título('Aula 20 de funções')'''

'''def soma(a, b):
    s = a + b
    print(s)

#Programa Principal
soma(4, 5)
soma(5, 6)
soma(6, 7)'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')'''

'''def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('Fim')


contador(1, 5, 9)
contador(2, 4, 8)'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi o valor {num} e são ao todo {tam} números')

contador(10, 9, 8, 7)
contador(6, 5, 4, 3)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [1, 3, 5, 7, 9, 11]
dobra(valores)
print(valores)'''


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 5)
