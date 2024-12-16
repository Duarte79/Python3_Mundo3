import os
import sys


# Função para adicionar cores ao texto
def colored(text, color):
    colors = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "fim": "\033[0m",
    }
    return colors[color] + text + colors["fim"]


# Limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    limpar_tela()
    print(colored("Digite um comando para ver o manual (ou 'FIM' para sair):", "ciano"))
    comando = input(">> ").strip()

    if comando.upper() == "FIM":
        print(colored("Encerrando o programa...", "vermelho"))
        break
    else:
        try:
            limpar_tela()
            print(colored(f"Manual para o comando '{comando}':", "amarelo"))
            help(comando)
        except Exception as e:
            print(colored(f"Erro: {e}", "vermelho"))

    input(colored("\nPressione Enter para continuar...", "verde"))
