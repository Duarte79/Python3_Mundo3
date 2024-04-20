#lista ordenada sem repetições

#cria uma lista vazia par armazenar os valores
lista = []
#lê 5 valores numéricos e os insere na lista na posição correta
for i in range(5):
    valor = int(input(f'Digite o {i+1}° valor: '))
#encotra a posição correta para inserir o valor na lista
    posição = 0
    while posição < len(lista) and valor > lista[posição]:
        posição+=1
#insere o valor na lista na posição correta
    lista.insert(posição, valor)
print('Lista ordenada', lista)