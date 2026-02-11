from random import randint
valores = list()


def sorteia():
    for n in range(1, 6):
        valores.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for v in valores:
        print(v, end=' ')
    print('Pronto!')


def somapar():
    soma = 0
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {valores}, temos {soma}')


sorteia()
somapar()


