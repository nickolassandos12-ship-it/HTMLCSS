#O wile em python é uma estrutura de repetição (loop) que executa um bloco de código enquanti uma condição for verdadeira.

import random # importa a biblioteca random para gerar números aleatórios

# gera um número aleatório entre 1 e 100
numero_secreto = random.randint (1,100)

# inicializar a variavél para contar as tentativas
tentativas = 0

# inicializar a variavél do palpite do jogador
palpite = 0

# exibe uma mensagem inicial para o jogador
print("👾 Bem-vindo ao jogo de adivinhação!")
print("tente adivinhar o número entre 1 e 100.")

# inicial um loop que continua até o jogador acertar o número
while palpite != numero_secreto:
    # solicitar ao usuário um número e converte para inteiro
    palpite = int(input("digite seu palpite: "))
    # incrementa o contador de tentativas
    tentativas += 1

    # verificar se o palpite é menor que o número secreto
    if palpite < numero_secreto:
        print("📉 Muito baixo! tente novamente.")
        # da uma dica ao jogador
    # verificar se o palpite é maior que o numero secreto
    elif palpite > numero_secreto:
        print("📈 Muito alto! tente novamente.")
        # da uma dica ao jogador

# sai do loop quando o palpite for igual ao número secreto
print(f"🎉 parabéns! você acertou o número{numero_secreto} em {tentativas} tentativas.")

# o while em pyrhon é uma estrutura de repetição (loop) que executa um bloco de código enquanto uma condição for verdadeira.20
