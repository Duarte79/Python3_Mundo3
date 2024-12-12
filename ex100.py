import random
numeros = []
def sorteia():
    for _ in range(5):
        numero = random.randint(1, 100)
        numeros.append(numero)
    print(f'Números sorteados: {numeros}')

def somaPar():
    soma = sum(numero for numero in numeros if numero %2 == 0)
    print(f'Soma dos valores pares: {soma}')


sorteia()
somaPar()
