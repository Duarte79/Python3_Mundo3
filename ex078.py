lista = []
#leitura dos valores
for i in range(5):
    valor = float(input(f'Digite o {i + 1}° valor: '))
    lista.append(valor)
#encontrar o maior e o menor valor
maior = menor = lista[0]
pos_maior = pos_menor = 0
for i in range(1, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        pos_maior = i
    elif lista[i] < menor:
        menor = lista[i]
        pos_menor = i
#exebir resultados
print(f'maior valor: {maior} (posição {pos_maior})')
print(f'menor valor: {menor} (posição {pos_menor}')


