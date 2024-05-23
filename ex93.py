jogador = dict()
partida = list()
jogador['nome'] = str(input('nome do jogador: '))
tot = int(input(f'Quantos partidos {jogador["nome"]} jagou? '))
for c in range(0, tot):
    partida.append(int(input(f'Quantos gols na pertida {c}? ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-='*30)
print('jogador')
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' na partida {i}, fez {v} gols')
print(f'foi um total de {jogador["total"]} gols')
