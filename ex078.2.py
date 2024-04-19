valores = []
for i in range(5):
    valor = float(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)
#encontrando o maior e o menor valor e suas posições
maior_valor = max(valores)
menor_valor = min(valores)
posição_maior = valores.index(maior_valor)+1
posição_menor = valores.index(menor_valor)+1
print(f'O maior valor digitado foi {maior_valor} na posição {posição_maior}')
print(f'O menor valor digitado foi {menor_valor} na posição {posição_menor}')