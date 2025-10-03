#diferenças entre as coleções:
# lista: permite elementos repetidos, mantém a ordem e é mutavel
# tulipa: similar à lista mas imutavel (não pode ser alterada após a criação).
# dicionário: armazena pares chave-valor, permitido acesso rápido pelos nomes das chaves.
# conjunto: não permite elementos duplicados e sua ordem não é garantida


# definição das coleções
lista = ["ford", "chevrolet", "toyota", "honda", "BMW"] #lista: estrutura mutável que permite elementos duplicados e pode ser alterada.

tulipa = ("ford", "chevrolet", "toyota", "honda", "BMW") # tupla: estrutura imutável ou seja seus valores não podem ser alterados após a criação

dicionario = {'sedan': "ford", 'esportivo': "chevrolet", 'suv': "toyota"} # dicionario: estrutura de chave-valor, permitido acesso direto por chave

conjunto = {"ford", "chevrolet", "toyota", "honda", "BMW"} # conjunto: estrutura que não permite elementos duplicados e não mantém oredm fixa.

# demonstrado a mutabilidade
print("llista antes da modificação", lista) # exibe a lista antes da alteração
lista[0] = "mercedes" # modificando o primeiro elemento da lista, permitido pois a lista é mutável
print("llista após da modificação", lista) # exibe a lista após a alteração

# tentando modificar uma tupla (isso resultará em erro se descomentando)
#tuppla [0] = "mercedes" # tuplas são imutaveis, então esta opercação não é permitida

# acessando elementos
print("elementos da lista no indice 1:", lista[1]) # acesso o segundo elemento da lista
print("elementos da lista no indice 1:", lista[1]) # acesso o segundo elemento da lista
print("valor da chave 'esportivo no dicionario:", dicionario['esportivo']) # acessa o valor associado a chave 'esportivo1' no dicionario

# adicionando elementos 
lista.append("audi") # adiciona "audi" a lista
print("lista apos adicionar elemento:", lista) # exibe a lista apos adição

dicionario['hatch'] = "hyundai" # adicina um novo par chave-valor ao dicionario
print("dicionario apos adição", dicionario) # exibe o dicionario apos adição

conjunto.add("audi") #adicionar "audi" ao conjunto se ja existir nao sera adicionado novamente
print("conjunto apos adição", conjunto) # exibe o conjunto apos adução 

# removendo elementos 
lista.remove("chevrolet") # remove "chevrolet" da lista.
print("lista apos remoção", lista) # exibe a lista apos remoção

del dicionario['sedan'] # remove a chave 'sedan' e seu valo do dicionario