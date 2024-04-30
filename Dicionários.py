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
pessoas['nome'] = 'Juliana'
for k, v in pessoas.items():
    print(k, '=', v)