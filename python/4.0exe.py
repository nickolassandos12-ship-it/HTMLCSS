def inicio():
    senha = 3353
    tentativa = 0
    tsenha = 0
    tentativas_restantes = 3

    print("Bem-vindo ao banco BRAZUCA")

    while tentativa < 3:
        tsenha = int(input("digite sua senha: "))

        tentativa += 1
        tentativas_restantes -= 1

        if tsenha == senha:
            print("Seja Bem-vindo")
            return

        else: print(f"Senha incorreta tente novamente você tem {tentativas_restantes}\n")

    print("você bloqueou sua conta, entre em contato com o suport\n")
        
inicio()