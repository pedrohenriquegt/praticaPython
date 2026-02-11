def fatorial(n, show=False):
    f = 1
    for v in range(n, 0, -1):
        if show:
            print(f'{v}', end='')
            if v > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= v
    return f


num = int(input('Digite um valor para descobrir seu fatorial: '))
resp = str(input('Voce quer ver a conta? ')).upper().strip()[0]
if resp in 'S':
    resp = True
else:
    resp = False
print(fatorial(num, show=resp))