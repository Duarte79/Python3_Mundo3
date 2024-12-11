from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(0.3)
    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont}', end='', flush=True)
            sleep(0.3)
            cont +=p
        print('fim')
    else:
        cont = i
        while cont >=f:
            print(f'{cont}', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('fim')


contador(1, 10 ,1)
contador(10, 0, 2)
print("agora é a sua vez de personalizar a contagem")
ini = int(input('Inicio'))
fim = int(input('Fim'))
passo = int(input('Passo'))
contador(ini, fim, passo)