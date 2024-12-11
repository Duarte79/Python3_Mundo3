#função contador
from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont += passo
        print('fim')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont -= passo
        print('fim')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim '))
passo = int(input('Passo '))
contador(inicio, fim, passo)