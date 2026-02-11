dados = dict()
gols = list()
jogadores = list()
c = 1

while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    for g in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {g + 1}? ')))
        dados['gols'] = gols[:]
    gols.clear()
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('ERRO! Valor Invalido! Quer continuar? ')).upper().strip()[0]
    if resp in 'N':
        break
print('=-' * 20)
print(f'{"cod":<5}{"Nome":<15}{"Gols":<13}{"Total":>7}')
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:<5}{v["nome"]:<15}{v["gols"]}{v["total"]:^10}')
print(len(jogadores))
while True:
    r = int(input('Mostrar levantamento de qual jogador? (999 para parar) '))
    if r >= len(jogadores):
        while r >= len(jogadores):
            print('Valor Invalido!')
            r = int(input('Mostrar levantamento de qual jogador? (999 para parar) '))
    if r == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[r]['nome']}')
    for k in jogadores[r]['gols']:
        print(f'No jogo {c} fez {k} gols.')
        c += 1
    c = 1

# Guanabara

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
## ---------- Codigo do cabecalho -------------
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
## --------------------------------------------
## ------------- Codigo da Tabela -------------
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
## --------------------------------------------
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
