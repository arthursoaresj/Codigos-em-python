import random
tentativas = 1
aleatorio = random.randint(0,10)
nome = str(input('Digite seu nome: ')).title()
print (f'Olá, {nome} Sou seu computador...')
print ('Acabei de pensar em um número entre 0 e 10')
print ('Sera que você consegue adivinhar!')
jogar = str(input('Deseja jogar? ')).strip().upper()[0]
if jogar == 'S':
    resp = int(input('Qual o seu palpite? '))
    while resp != aleatorio:
        if resp < aleatorio:
            print ('Mais... Tente novamente.')
            resp = int(input('Qual o seu palpite? '))
        if resp > aleatorio:
            print ('Menos... Tente novamente.')
            resp = int(input('Qual o seu palpite? '))
        tentativas += + 1
    if resp == aleatorio:
        print (f'Acertou! com {tentativas} tentativas.')
        if tentativas > 5:
            print('Demorou acertar ein')
        elif tentativas < 2:
            print ('Foi rápido')

else:
    print ('Tudo bem!')