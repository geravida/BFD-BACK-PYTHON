#1
'''estoque = ['camiseta', 'calça', 'meia', 'jaqueta']
estoque.append('boné')
estoque.remove('calça')
print(estoque)

#2
lista_alunos = ['Bruno','Ana','Carlos', 'Denise','Felipe']
print(lista_alunos)
lista_alunos.sort(reverse=True)
print(lista_alunos)
lista_alunos.index("Felipe")
print(lista_alunos.index("Felipe"))
lista_alunos.index('Ana')
print(lista_alunos.index('Ana'))
'''
#3
vendas_semana = (1200,1500,1100,2000,2500,1800,1300)
vendas = sum(vendas_semana)
print(vendas)
menor_venda= min(vendas_semana)
print(menor_venda)
vendas_semana.index(menor_venda)
print(vendas_semana.index(menor_venda))

Vendas_total= 0
for Vendas in vendas_semana:
    Vendas_total+=Vendas 
print(Vendas_total)

Vendas_menor= 9999
for Vendas in vendas_semana:
    if Vendas_menor >= Vendas: 
        Vendas_menor = Vendas
print(Vendas_menor)           
    




'''
#Tupla
#vazia
modelo_carros=()
#valores imutáveis
modelo_carros = ('Toyota','Corolla', 2025)

#acessando a Tupla
print(modelo_carros[1])
print(modelo_carros[0:2])


'''