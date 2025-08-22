import random
print('============================================')
print ('           COMPUTADOR PENSANTE             ')
print('============================================')
print ('Tente adivinhar o [número que eu pensei entre 0 e 5')
jogar=input('Deseja jogar?[S/N]').upper()
if jogar == 'S':
    num=random.randint(0,5)
    print('Já pensei')
    resposta=int(input('Qual o número? '))
    if resposta == num:
        print ('Parabéns! você acertou!')
    else:
        print('Você errou')
else:
    print('Tudo bem!')