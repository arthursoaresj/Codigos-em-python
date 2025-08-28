import random
print('=-'*20)
print ('           COMPUTADOR PENSANTE             ')
print('=-'*20)
print ('Tente adivinhar o número que eu pensei entre 0 e 5')
jogar=input('Deseja jogar?[S/N] ').upper()
if jogar == 'S' or jogar == 'SIM':
    num=random.randint(0,5)
    print('Já pensei')
    resposta=int(input('Qual o número? '))
    if resposta == num:
        print ('Parabéns! você acertou!')
    else:
        print('Você errou, eu pensei no número {}'.format(num))
else:
    print('Tudo bem!')
