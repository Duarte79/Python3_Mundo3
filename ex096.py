def area(largura, comprimento):
    """
    Calcula a área de um terreno retangular.

    :param largura: Largura do terreno
    :param comprimento: Comprimento do terreno
    :return: Área do terreno
    """
    return largura * comprimento


# Exemplo de uso
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
print(f"A área do terreno é {area(largura, comprimento)} metros quadrados.")