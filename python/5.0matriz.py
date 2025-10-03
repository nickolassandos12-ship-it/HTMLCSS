import random
def inicio():
    frutas = "maçã", "banana", "uva", "laranja", "pera", "manga", "abacaxi", "melancia", "morango"
    matriz = []

    for i in range(3):

        vetor = random.sample(frutas, 3)
        matriz.append(vetor)
    
    print("matriz gerada com frutas:")

    for linha in matriz:

            fruta = input("\n digite o nome de uma fruta para busca na matriz: ")

    encontrado = False

    for i, linha in enumerate (matriz):

        if fruta in linha:

            print(f"A fruta {fruta} está na posição: linha{i + 1}, colona{linha.index(fruta) + 1}")

            encontrado = True

    if not encontrado:
    
        print(f"A fruta {fruta} não foi encontrada na matriz.")

inicio()