"""
Objetivo:
Simular Login com usuario e senha fixos.
"""
senha_correta = "1234"
usuario_correto = "Pedro"
tentativas = 3

while tentativas > 0:
    usuario = input("Digite seu Usuario: ")
    senha = input("Digite sua Senha (Apenas Numeros): ")

    if senha != senha_correta or usuario != usuario_correto:
        tentativas -= 1
        print("Senha ou Usuario Incorretos!")
        print("Tentativas Restantes: {}".format(tentativas))
    else:
        print("Bem Vindo, {}".format(usuario))
        break

if tentativas == 0:
    print("Conta Bloqueada, Tente novamente mais tarde")

print("Fim do Programa!")
