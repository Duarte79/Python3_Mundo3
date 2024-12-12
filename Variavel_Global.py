# Variável Global
contador = 10

def adicionar():
    # Variável Local
    contador_local = 5
    print("Valor de 'contador_local' dentro da função:", contador_local)

    global contador
    contador += 1
    print("Valor de 'contador' dentro da função:", contador)

# Chamando a função
adicionar()

# Imprimindo valor das variáveis fora da função
print("Valor de 'contador' fora da função:", contador)
