from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('=-'*20)
print ('               JOKENPO')
print ('=-'*20)
nome=str(input('Qual o seu nome? ')).title().strip()
resp=str(input('Bem vindo, {}\nDeseja jogar Jokenpo?[S/N] '.format(nome))).strip().upper()
if resp == 'S':

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
    print ('Computador jogou \033[4m{}\033[m'.format(itens[computador]))
    print ('{} jogou \033[4m{}\033[m'.format(nome,itens[jogador]))
    print ('=-'*11)
    if computador == 0: #COMPUTADOR JOGOU PEDRA
        if jogador == 0:
            print ('EMPATE')
        elif jogador == 1:
            print ('{} VENCEU'.format(nome).upper())
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
            print ('{} VENCEU'.format(nome).upper())
        else:
            print('Jogada inválida')

    if computador == 2: #COMPUTADOR JOGOU TESOURA
        if jogador == 0:
            print ('{} VENCEU'.format(nome).upper())
        elif jogador == 1:
            print ('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print ('EMPATE')
        else:
            print('Jogada inválida')


else:
    print ('Tudo bem!')
