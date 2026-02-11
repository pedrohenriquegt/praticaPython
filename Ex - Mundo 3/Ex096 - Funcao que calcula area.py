def area(a, b):
    tot = a * b
    print(f'A area de um terreno {a}x{b} é de {tot}m²')


def lin():
    print('-' * 30)


lin()
print('     CONTROLE DE TERRENO     ')
lin()

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)