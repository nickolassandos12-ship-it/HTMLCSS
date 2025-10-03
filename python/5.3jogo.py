import random # importa a biblioteca random para escolher uma palavra aleatoria

# lista de palavras possiveis para o jogo
palavras = ["robertocarlos", "tiririca", "arnowd", "pele", "brasil", "toguro"]

# escolje uma palavra aleatoria da lista
palavra = random.choice(palavras)

#cria uma lista com "_" para cada letra da palavra(será mostrada ao jogador)                                
letras_descobertas = ["_"] * len(palavra)

#lista que vai guardar as letras erradas que o jogador digitar
letras_erradas= []

# define o numero maxio de tentativas(erros permitidos)
tentativas = 12

# mensagem inicial do jogo
print("bem-vindo ao jogo da forca!.")
print("adivinhe a palavra letra por letra.")

#laço que repete o numero de tentativas permitidas
for tentativa in range(1, tentativas + 1):
    # mostra a palavra atual com as letras descobertas ate o momento
    print("\npalavra:", " ".join (letras_descobertas))

    #mostra as letras que o jogador ja errou
    print("letras erradas", " ".join(letras_erradas))

    #pede ao jogador para digiar uma letra
    letra = input(f"tentativa {tentativa}/{tentativas} - digite uma letra: ").lower()

    # verificar se a letra digita esta na palavra
    if letra in palavra:
        # substitui os "_" pela letra correta nas posições correspondentes
        for i in range(len(palavra)):
            if palavra [i] == letra:
                letras_descobertas[i] = letra
        print("letra correta!")
    else:
        # se a letra estiver errada, adiciona na lista de letras erradas

        letras_erradas.append(letra)
        print("letra incorreta")

    #verificar se todas as letras foram descobertas
    if "_" not in letras_descobertas:
        print ("\n parabens voce acertou a palavra:", palavra)
        break # encerrar o laço se o jogador vencer
else:
    # se o jogador nao acertar apos todas as tentativas perde o jogo
    print("\n voce perdeu! a palavra era:", palavra)