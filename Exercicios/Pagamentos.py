print ('-='*20)
print ('LOJINHA DO ARTHUR')
print ('-='*20)
valor=float(input('Qual o valor da compra: R$'))
print ('FORMAS DE PAGAMENTO')
print ([ 1 ],'à vista, no dinheiro')
print ([ 2 ],'à vista, no cartão')
print ([ 3 ],'2x no cartão')
print ([ 4 ],'3x ou mais no cartão')
resp=input('Qual a forma de pagamento? ')
if resp == '1':
    print (f'R${valor} à vista no dinheiro, o valor final será de R${valor-(valor*0.10):.2f} devido ao desconto de 10%')
elif resp == '2':
    print (f'R${valor} à vista no cartão, o valor final será de R${valor-(valor*0.05):.2f} devido ao desconto de 5%')
elif resp == '3':
    print(f'Compra de R${valor} parcelada em 2x sem juros\nFicara R${valor/2:.2f} por mês')
elif resp == '4':
    parcelas=int(input('Quantas parcelas? '))
    print (f'Sua compra será parcelada em {parcelas} vezes de R${(valor + (valor * 0.20)) / parcelas:.2f} com juros de 20%')
    print(f'Sua compra de R${valor} vai custar R${valor+(valor*0.20):.2f} ao todo')
