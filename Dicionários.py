'''pessoas = {'Nome': 'Duarte', 'Sexo': 'M', 'Idade': 45}
print(pessoas)
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''

pessoas = {'nome': 'Duarte', 'sexo': 'M', 'idade': 45}
'''for k, v in pessoas.items():
    print(k, '=', v)'''
'''for k in pessoas.keys():
    print(k)'''
'''del pessoas['nome']
for k, v in pessoas.items():
    print(k, '=', v)'''
'''pessoas['nome'] = 'Juliana'
for k, v in pessoas.items():
    print(k, '=', v)'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0] ['uf'])
print(brasil[1] ['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa:' ))
    estado['sigla'] = str(input('sigla do estado:' ))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
