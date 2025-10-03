#criando uma lista com nomes de frutas
frutas = ["maçã" , "banana" , "uva" , "laranja"]

# exibindo a lista completa
print("lista de frutas", frutas)


# exemplo 2 
#lista com numeros inteiros
numeros = [10,20,30,40,50]

#soma de todos os elementos da lista
soma = sum(numeros)

# exibindo o resultado
print("a soma dos numeros é:" , soma)


#exemplo3
# lista vazia
nomes = []

# adicionando nomes a lista
nomes.append("Ana")
nomes.append("Carlos")
nomes.append("Beatriz")

# mostrando os nomes inseridos
print("nomes na lista:", nomes)


#exemplo4
# lista com cores
cores = ["azul", "verde", "amarelo", "vermelho"]

# acessando o primeiro elemento (indice 0)
print("A primeira cor é:", cores [0])

# acessando o primeiro elemento (indice -1)
print("A ultima cor é:", cores [-1])

# exemplo5
# lista vazia para armazenar os pares
pares = []

# laço que vai de 2 ate 20, de 2 em 2
for i in range(2, 21, 2):
    pares.append(i) #adicionar o numero na lista

# mostrando a lista de pares
print("Números pares de 2 a 20", pares)
