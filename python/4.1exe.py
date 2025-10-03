def inicio():
    senha = 3353
    tentativa1 = 0
    tentativa2 = 0
    tsenha = 0
    tentativas_senha = 3
    tentativas_usuario = 3
    usuario = 10
    tusuario = 0

    print("Bem-vindo ao banco BRAZUCA")

    while tentativa1 < 3 :
        tusuario = int(input("digite seu usuário: "))

        tentativa1 += 1
        tentativas_usuario  -= 1
        
        if tusuario == usuario:
            print("Seja Bem-vindo")
            
            while tentativa2 < 3:
                tsenha = int(input("digite sua senha: "))
                tentativa2 += 1
                tentativas_senha -= 1

                if tsenha == senha:
                    print("Seja Bem-vindo")
                    return

                else: print(f"Senha incorreta tente novamente você tem {tentativas_senha}\n")

            print("você bloqueou sua conta, entre em contato com o suport\n")
            
        else: print(f"usuário incorretp tente novamente você tem {tentativas_usuario}\n")
        
    print("você bloqueou sua conta, entre em contato com o suport\n")    
        
inicio()