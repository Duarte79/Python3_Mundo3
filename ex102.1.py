def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.

    Args:
        numero (int): O número para calcular o fatorial.
        show (bool, optional): Se True, mostra o processo de cálculo. Defaults to False.

    Returns:
        int: O fatorial do número.
    """

    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
        if show:
            print(f"{i}! = {fatorial}")
    return fatorial


# Exemplo de uso:
num = int(input("Digite um número para calcular o fatorial: "))
mostrar_processo = input("Deseja ver o processo de cálculo? (sim/não): ")
mostrar_processo = mostrar_processo.lower() == 'sim'

resultado = fatorial(num, mostrar_processo)
print(f"O fatorial de {num} é {resultado}")