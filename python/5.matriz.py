import random  # importa a biblioteca random para gerar elementos aleatórios

# gerar matriz 3x3 com nomes de frutas
frutas = ["maçã", "banana", "uva", "laranja", "pera", "manga", "abacaxi", "melancia", "morango"] #lista com nomes de frutas

matriz = [] #cria uma lixta vazia para armazenar a matriz

for i in range(3): # loop para criar 3 linhas na matriz

    vetor = random.sample(frutas, 3) # selecionar aleatorioamente 3 frutas da lista

    matriz.append(vetor) # adicionar esse vetor como uma linha na matriz

# exibir a matriz

print("matriz gerada com frutas:") # mensagem para exibir a matriz

# o i é uma variável de cibtrike de laço for.

# a função range(3) gera os números 0 , 1 e 2.

# assim, o laço for será executado 3 vezes, uma para cada número

# a cada repetição, o i assume um desses valores:

# primeira repetição: i = 0

# segunda repetição: i = 1

# terceira repetição: i = 2

for linha in matriz: # loop para percorrer cada linha da natriz

    # verificar se uma fruta está na matriz
    fruta = input("\n digite o nome de uma fruta para busca na matriz: ") # solicitar uma fruta ao usuário

encontrado = False  # inicializar uma variável para verificar se a fruta foi encontrada

for i, linha in enumerate (matriz): # loop para percorrer cada linha com seu índice
    
    if fruta in linha: # verificar se a fruta está na linha atual

        print(f"A fruta {fruta} está na posição: linha{i + 1}, colona{linha.index(fruta) + 1}") # exibe a posição da fruta encontrada

        encontrado = True # marca que a fruta foi encontrada

if not encontrado: # verifica se a fruta não foiencontrada

    print(f"A fruta {fruta} não foi encontrada na matriz.")  # mensagem caso a fruta não seja encontrada na matriz