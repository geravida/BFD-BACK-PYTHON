
produtos = ['feijão', 'carne', 'peixe', 'manteiga', 'café', 'oléo']
'''
print (produtos [0])

#fatiando a lista

print(produtos[0:3])

#formas de manipular lista
#add novos valores
#append

produtos.append('bolacha')

print(produtos)

#insert

produtos.insert(0,'iogurte')
print(produtos)

#remover produtos da lista
#remove

produtos.remove('feijão')
print(produtos)

#pop
produtos.pop (1)
print(produtos)

#ordenando produtos
produtos.sort()
print(produtos)

#reverse
produtos.reverse()
print(produtos)

#descobrindo quantas vezes o elemento na lista
print(produtos.count('oleo'))
'''

#index
#posição

print(produtos.index('peixe'))

#descobrindo a quantidade de elementos na lista
#len

print(len(produtos))

#del
del produtos[2]
print(produtos)
del produtos [0:2]
print(produtos)

#clean
produtos.clear()
print(produtos)
