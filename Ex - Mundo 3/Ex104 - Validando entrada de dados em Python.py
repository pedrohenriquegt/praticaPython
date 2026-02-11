def leiaint(text):
    num = input(text)
    while not num.isnumeric():
        print(f'\033[31mERRO! Digite um numero inteiro valido!\033[m')
        num = input(text)
    return int(num)


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')


