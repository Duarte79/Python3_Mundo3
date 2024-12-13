def voto(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


ano_nascimento = int(input('Digite o ano de nascimento: '))
print(f'Com o ano de {ano_nascimento}, seu status de voto é: {voto(ano_nascimento)}')
