# Tipos de funções em Python: 

# 1 - Função tradicional:
# def calcular_imposto (preco):
#   return preco * 0.2

# 2 - Função Lambda (função anônima e mais direta):
# calcular_imposto2 = lambda preco * 0.2

precos = [100, 5000, 690, 750, 6000]

prco_com_imposto = list(map(lambda x: x + (x * 0.2), precos))

print(prco_com_imposto)