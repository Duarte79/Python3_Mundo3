#valores únicos em uma lista
#cria uma lista vazia para armazenar os valores
lista = []
#loop para ler os valores do usuário
while True:
    valor = int(input('Digite um valor (ou 0 para sair): '))
#sai do loop se o valor for 0
    if valor == 0:
        break
#verificar se o valor já está na lista
    if valor in lista:
        print('valor já existe na lista')
    else:
#adiciona o valor à lista
        lista.append(valor)
#ordena a lista em ordem crescente
lista.sort()
#exibe os valores ínicos da lista
print('valores únicos digitados', lista)
