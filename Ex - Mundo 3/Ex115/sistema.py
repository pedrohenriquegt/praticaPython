from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu('\033[0;32mSua opcao: \033[m')
    if opcao == 1:
        lin('Opcao 1')
        lerArquivo(arq)
        sleep(1)
        continue
    if opcao == 2:
        lin('Opcao 2')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
        sleep(1)
        continue
    if opcao == 3:
        lin('Finalizando...')
        sleep(1.5)
        break
print('Ate logo!')