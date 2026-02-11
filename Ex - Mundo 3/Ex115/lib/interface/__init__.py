from time import sleep


def lin(txt):
    print('-' * 43)
    print(txt.center(43))
    print('-' * 43)


def menu(op):
    while True:
        lin('MENU PRINCIPAL')
        print(f'\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas\033[m')
        print(f'\033[0;33m2\033[m - \033[0;34mCadastrar nova pessoa\033[m')
        print(f'\033[0;33m3\033[m - \033[0;34mSair do sistema\033[m')
        print('-' * 43)
        try:
            o = int(input(op))
            if o > 3:
                print('\033[0;31mERRO! Digite uma opcao dentro das disponiveis! \033[m')
                continue
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite uma Opcao valida! \033[m')
            sleep(1)
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuario saiu do programa! \033[m')
            break
        return o








