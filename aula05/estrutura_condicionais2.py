'''
import random

semaforo = random.choice (['vermelho', 'amarelo', 'verde'])

if semaforo == 'vermelho':
    print ('Não passa...')
if semaforo == 'amarelo':
    print (' Pode passar, porém tenha cuidade...')
if semaforo == 'verde':
    print ( ' Pode passar...')

import random

# semaforo = random.choice (['vermelho', 'amarelo', 'verde'])
semaforo = random.choice (['vermelho', 'amarelo', 'verde'])

if semaforo == 'vermelho':
    print ('Não passa...')
elif semaforo == 'amarelo':
    print (' Pode passar, porém tenha cuidade...')
else: 
    print ( ' Pode passar...')



idade_minima = 18

idade_usuario = int(input (' digite sua idade : '))

if idade_usuario >= idade_minima :
    print (' Você é maior de idade.')
else:
    print(' Você é menor de idade. ')
    
idade_minima = 18

idade_usuario = int(input (' digite sua idade : '))

if idade_usuario >= idade_minima :
    print (' Você é maior de idade.')
elif idade_usuario < idade_minima and idade_usuario >= 16:
    print(' O usuario é menor e tem 16 ou 17 anos.')
else:
    print(' O usuario é menor de idade.')
   
comida = 'feijão carioca'

match comida:
    case 'lasanha':
        print (' que lasanha gostosa!')
    case 'pirão':
        print(' que pirão gotoso!')
    case 'strogonoff':
        print(' Que strogonoff gostoso!')
    case 'feijão carioca':
        print(' Que feijão carioca gostoso!')
    case _ :
        print(' comando invalido.')
        
variavel = 0
while variavel < 10:
    print(variavel)
    input()
    variavel += 1
    
lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    print(valor)
    input()

numero = 2

for valor in range(0,11):
    print(f'{numero}x{valor + 1} = {numero* (valor +1)}')
    input()
'''
numero = 2
variavel_temporaria = 1
while variavel_temporaria <= 10:
    print(numero * variavel_temporaria)
    variavel_temporaria += 1
    input()

print('O loop ecerrou.')


