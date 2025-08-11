'''
print('Olá, mundo!')

nome= input('insira seu nome?')
print(f'Olá,{nome} Tudo bem comvocê?')

numero=int(input('qual o numero?'))
print(f'O número informado foi {numero}')

nome= input('insira seu nome?')
sobrenome= input('insira o sobrenome?')
idade= input('insira sua idade?')
print(f'{nome}')
print(f'{sobrenome}')
print(idade)

nome_filme= input('diga o nome do filme?')
genero_filme= input('diga o gênero do filme?')
print(f'{nome_filme}\n{genero_filme}')

palavra_1= input('diga a palvra 1?')
palavra_2= input('diga a palvra 2?')
palavra_3= input('diga a palavra 3?')
palavra_4= input('diga a palavra 4?')
print ( f'{palavra_1} {palavra_2} {palavra_3} {palavra_4}')

CIDADE= input ('diga a cidade?')
ESTADO= input ('diga o nome do estado?')
print (f'{CIDADE}\n{ESTADO}')

import datetime

nome_usuario= (' Geralda ')
hora_atual= datetime.datetime.now()
print (f' Olá, {nome_usuario}! Agora são {hora_atual.strftime('%H:%M')} horas.')

nome_produto= input(' digite o nome do produto?')
preço_produto= float(input('digite o preço do produto?'))
print(f' O produto {nome_produto} custa R$ {preço_produto:.2f}. ')
'''
nome_cidade= input('diga a cidade?')
sigla_pais= input( 'diga a sigla?')

print(f'Eu gostaria de visitar {nome_cidade} , {sigla_pais}.')
