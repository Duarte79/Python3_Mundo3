def maior(*valores):
    maior_valor = None
    for valor in valores:
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
    print(f'O maior valor é: {maior_valor}')


maior(5, 10, 3, 8, 2)
maior(1, 2, 3, 4, 5)
maior(-1, -5, -3, -10)