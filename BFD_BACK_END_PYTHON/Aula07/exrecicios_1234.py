'''
#1
dados_funcionario= ( 'Ana Souza', 'Gerente', 8500.00)
nome= dados_funcionario[0]
print(nome)
cargo= dados_funcionario[1]
print(cargo)
salario= dados_funcionario [2]
print(salario)


#2
venda= ('caderno',15)
qtd= (venda [1])
print(qtd * 25)
'''

#3

arquivos= ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')
contador=0
for extencao in arquivos:
    if extencao.endswith('.pdf'): 
       contador+=1 
print(contador)       