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
    print ('R${} à vista no dinheiro, o valor final será de R${:.2f} devido ao desconto de 10%'.format(valor,valor-(valor*0.10)))
elif resp == '2':
    print ('R${} à vista no cartão, o valor final será de R${:.2f} devido ao desconto de 5%'.format(valor,valor-(valor*0.05)))
elif resp == '3':
    print('Compra de R${} parcelada em 2x sem juros\nFicara R${:.2f} por mês'.format(valor,valor/2))
elif resp == '4':
    parcelas=int(input('Quantas parcelas? '))
    print ('Sua compra será parcelada em {} vezes de R${:.2f} com juros de 20%'.format(parcelas,(valor+(valor*0.20))/parcelas))
    print('Sua compra de R${} vai custar R${:.2f} por mês'.format(valor,(valor+(valor*0.20))))