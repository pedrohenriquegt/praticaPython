def voto(n):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - n
    if idade > 70 or 18 > idade >= 16:
        return f'Com {idade} anos. Voto Opcional'
    elif idade >= 18:
        return f'Com {idade} anos. Voto OBRIGATORIO'
    else:
        return f'Com {idade} anos. VOTO NEGADO'


print('-' * 30)
ano = int(input('Em que ano voce nasceu? '))
print(voto(ano))