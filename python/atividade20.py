# loguin
def inicio():
    senha = 3353
    tsenha = 0
    tentativas = 0
    tentativas_restantes = 4
    print("Bem-vindo ao SLA")
    while tentativas < 4:
        tsenha = int(input("digite a senha para acessar a conta "))

        tentativas += 1
        tentativas_restantes -= 1
        
        if tsenha == senha:
            print("acesso permitido")
            return 
        
        else: print(f"acesso negado, você tem mais {tentativas_restantes} tentativas")
            
    print("Você bloqueou a sua conta entre em contato com o suporte")

inicio()