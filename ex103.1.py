def ficha(nome='<desconhecido>', gols=0):
  """
  Função que cria uma ficha de jogador e retorna um dicionário.

  Args:
    nome (str, opcional): Nome do jogador. Padrão: '<desconhecido>'.
    gols (int, opcional): Quantidade de gols marcados. Padrão: 0.

  Returns:
    dict: Dicionário contendo as informações do jogador.
  """

  if not isinstance(gols, int) or gols < 0:
    raise ValueError('A quantidade de gols deve ser um número inteiro não negativo.')

  return {'nome': nome, 'gols': gols}

# Exemplo de uso:
jogador = ficha('Cristiano Ronaldo', 800)
jogador = ficha()
jogador = ficha(nome='Cristiano')
jogador = ficha(gols=1000)
print(jogador)  # {'nome': 'Cristiano Ronaldo', 'gols': 800}