'''
a=10
b=3

resultado_and= (a>5) and (b<5)
resultado_or= (a>15) or (b<5)
resultado_not= not (a>5)

print (f' (a>5) and (b<5): {resultado_and} \n (a>15) or (b<5): {resultado_or} \n not(a>5): {resultado_not}')

# Definindo as variaveis que representam as condições da compra:
valor_da_compra= 90
esta_usando_cupom= True
e_membro_premium= False

tem_direito_a_frete_gratis= (valor_da_compra > 100 and not esta_usando_cupom) or e_membro_premium  

print(f' o cliente tem direito a frete grátis? {tem_direito_a_frete_gratis}')
'''
tem_wifi= False
tem_dados_moveis= True
resultado_or=(tem_wifi  or tem_dados_moveis)

print(f'O celular pode se conectar à internete? {resultado_or}.')
