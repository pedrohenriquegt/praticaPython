from time import sleep


def lin():
    print('-=' * 20)


def contadorguanabara(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print('Fim')


def contador(inicio, fim, passo):
    lin()
    if passo < 0:
        passo = abs(passo)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    if inicio > fim and passo > 0:
        fim -= passo
        passo = -passo
    if fim > inicio:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
lin()
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
pa = int(input('Passo: '))
contador(ini, fi, pa)