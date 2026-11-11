blocostotal = int(input("Digite a quantidade de blocos totais: "))
alturapiramide = 0
camadaatual = 1
#entender a formula por trás do problema
#se tenho 6 blocos, a base é 3, acima 2, acima 1...
#tenho que descobrir a altura da piramide(Nmr camadas concluidas) 
# e o valor da base também.

while blocostotal >= camadaatual:
    blocostotal -= camadaatual 
    camadaatual += 1
    alturapiramide += 1


print("A altura da piramide é: ",alturapiramide)