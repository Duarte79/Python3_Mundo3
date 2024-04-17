numeros = []
while True:
    numero = int(input('Digite um número (0 para sair): '))
    if numero == 0:
        break
    numeros.append(numero)
quantidade_numeros = len(numeros)
numeros.sort(reverse=True)
valor_5_presente = 5 in numeros
print(f'Quantidade de números digitados {quantidade_numeros}')
print(f'lista de valores ordenados de forma decrescente {numeros}')
print(f'O valor 5 {'está' if valor_5_presente else 'não está'} na lista')