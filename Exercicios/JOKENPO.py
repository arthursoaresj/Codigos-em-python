from random import randint
from time import sleep
denovo='S'
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('=-'*20)
print ('               JOKENPO')
print ('=-'*20)
nome=str(input('Qual o seu nome? ')).title().strip()
resp=str(input(f'Bem vindo, {nome}\nDeseja jogar Jokenpo?[S/N] ')).strip().upper()[0]
if resp == 'S':
    while denovo != 'N':

        print ('''Suas ações: 
        [0] Pedra
        [1] Papel
        [2] Tesoura''')
        jogador = int(input('Qual a sua jogada? '))
        print ('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print ('=-'*11)
        print (f'Computador jogou \033[4m{itens[computador]}\033[m')
        print (f'{nome} jogou \033[4m{itens[jogador]}\033[m')
        print ('=-'*11)
        if computador == 0: #COMPUTADOR JOGOU PEDRA
            if jogador == 0:
                print ('EMPATE')
            elif jogador == 1:
                print (f'{nome.upper()} VENCEU')
            elif jogador == 2:
                print ('COMPUTADOR VENCEU')
            else:
                print('Jogada inválida')

        if computador == 1: #COMPUTADOR JOGOU PAPEL
            if jogador == 0:
                print ('COMPUTADOR VENCEU!')
            elif jogador == 1:
                print ('EMPATE')
            elif jogador == 2:
                print (f'{nome.upper()} VENCEU')
            else:
                print('Jogada inválida')

        if computador == 2: #COMPUTADOR JOGOU TESOURA
            if jogador == 0:
                print (f'{nome.upper()} VENCEU')
            elif jogador == 1:
                print ('COMPUTADOR VENCEU!')
            elif jogador == 2:
                print ('EMPATE')
            else:
                print('Jogada inválida')
        denovo = str(input('Deseja jogar novamente?[S/N] ')).strip().upper()[0]
        if denovo == 'N':
            print('Tudo bem!')

else:
    print ('Tudo bem!')
