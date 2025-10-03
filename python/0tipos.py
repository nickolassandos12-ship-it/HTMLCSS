# Tipos de dados em Python

# 1. Tipo None
nada = None
print("nonetype:", nada, type(nada))

# 2. tipo booleano
verdadeiro = True
falso = False
print("boolean:", verdadeiro, type(verdadeiro))

# 3. Tipos numéricos
inteiro = 10
ponto_flutante = 3.14
numero_complexo = 2+3j
print("int:", inteiro, type(inteiro))
print("float:", ponto_flutante , type(ponto_flutante))
print("complex:", numero_complexo, type(numero_complexo))

# 4. tipo string
texto = "olá, mundo!"
print("string:", texto, type(texto))

# 5. tipo lista (list)
lista = [1, 2, 3, "quatro, 5.0"]
print("list:", lista, type(list))

# 6. tipo tupla (tuple)
tupla = (1, 2, 3)
print("tuple:"), tupla,type(tupla)

# 7. tipo conjunto (set)
conjunto = {1, 2, 3, 2}
print("set:", conjunto, type(conjunto))
# elementos duplicados são removidos

# 8. tipo dicionário (dict)
dicionario = {"nome": "joão", "idade": 30}
print("dict", dicionario, type(dicionario))