valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
ced = 50
tot = 1
while True:
    if total >= ced:
        total -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'Total de {tot} celulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if total == 0:
            break
