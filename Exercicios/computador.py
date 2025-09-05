import random
resp = 'S'
print('=-'*20)
print ('           COMPUTADOR PENSANTE             ')
print('=-'*20)
print ('Tente adivinhar o número que eu pensei entre 0 e 5')
jogar=input('Deseja jogar?[S/N] ').strip().upper()[0]
if jogar == 'S' or jogar == 'SIM':
    while resp != 'N':
        numero=random.randint(0,5)
        num=random.randint(0,5)
        print('Já pensei')
        resposta=int(input('Qual o número? '))
        if resposta == num:
            print ('Parabéns! você acertou!')
        else:
            print(f'Você errou, eu pensei no número {num}')
        resp=input('Deseja jogar novamente?[S/N] ').strip().upper()[0]
        if resp == 'N':
            print('Tudo bem!')
else:
    print('Tudo bem!')
