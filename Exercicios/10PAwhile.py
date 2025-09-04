from time import sleep
print ('GERADOR DE PA')
print ('-='*20)
n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
total = 0
mais = 10
print ('Calculando...')
sleep(1)
while mais != 0:
    total += mais
    while cont != total:
        print (n, '-> ', end = '')
        n += razao
        cont += 1
    print ('PAUSA')
    mais = int(input('Quantos termos você quer mostra a mais? '))
    if mais != 0:
        print('Calculando...')
        sleep(1)
print ('FINALIZANDO...')
print (f'Ao todo foram {total} termos mostrados.')