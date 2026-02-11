def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um numero inteiro valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados encerrada.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            nf = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um numero real valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados encerrada.')
            return 0
        else:
            return nf


num = leiaint('Digite um numero Inteiro: ')
numreal = leiafloat('Digite um numero Decimal: ')
print(f'O valor digitado inteiro foi {num} e o real foi {numreal}')