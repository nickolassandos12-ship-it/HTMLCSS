def inicio():
    
    print("semáforo")
    
    semaforo = input(print("digite a cor do semáforo \n"))
   

    if semaforo == "verde" :
            print(f"O semáforo está {semaforo} pode passar")

    elif semaforo == "amarelo":
            print(f"O semáforo está {semaforo} reduza a velocidade e fique atento")

    elif semaforo == "vermelho":
           print(f"O semáforo está {semaforo} pare o carro e espere o semáforo ficar verde")

    else:
           print("cor não encontrada, verifique a cor e escrva novamente")


inicio()