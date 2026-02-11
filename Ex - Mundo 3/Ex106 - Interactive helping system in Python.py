def lin(cor=0, text=''):
    print(f'\033[0;30;{cor}m', '~' * (len(text) + 3))
    print(f'  {text}')
    print('~' * (len(text) + 4))


while True:
    lin(42, 'SISTEMA DE AJUDA PyHELP')
    p = str(input('\033[mFuncao ou Biblioteca > '))
    if p == 'fim' or p == 'FIM' or p == 'Fim':
        break
    lin(46, f'Acessando o manual de comando {p}')
    print("\033[48;2;255;255;255m")
    print(help(p))
lin(41, 'Ate Logo!!')