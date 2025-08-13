'''
a=2
b=4

soma= a + b
subtracao= a-b
multiplicacao= a * b
divisao= a / b
divisao_inteira= a // b
modulo= a % b
exponenciacao= a ** b

print( f'soma: {soma}')
print( f' subitração: {subtracao}')
print( f' multipliocação: {multiplicacao}')
print( f'divisão: {divisao}')
print( f'divisão inteiro: {divisao_inteira}')
print( f'modulo: {modulo}')
print( f'exponenciacao: {exponenciacao}')

valor_1= int(input( 'digite o valor:'))
valor_2= int(input(' digite outro valor:'))

soma= valor_1 + valor_2
subtracao= valor_1 - valor_2

print(f' soma: {soma}')
print(f' subtração: {subtracao}')

salario_bruto= 2500
TAXA_IMPOSTO= 0.10
TAXA_BONUS= 0.05

salario_liquido = salario_bruto - salario_bruto* TAXA_IMPOSTO + salario_bruto* TAXA_BONUS

print(f' O salário loquido calculado é de R$ {salario_liquido:.2f}')

saldo= 1000
saldo += 50
print(f'saldo após o deposito:{saldo}')

saldo-= 25
print(f' Saldo após o saque: {saldo}')

estoque= 10
estoque*= 2
print(f' Estoque dobrado: {estoque}')

total_vendas= 500
total_vendas/= 2
print(f' total de vendas dividido: {total_vendas}')
'''
idade_minima= 18

idade_usuario=int(input('digite sua [idade:'))
print(f' O usuario é maior de iadde?{idade_usuario >= idade_minima}')
print(f'O usuário é menor de idade{idade_usuario <idade_minima}.')

