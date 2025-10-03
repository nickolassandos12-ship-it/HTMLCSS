def inicio():

    print("vamos calcular o seu IMC")

    peso = int(input("Digite seu peso em KG \n"))
    altura = float(input("digite sua altura em metros \n"))

    resultado = peso / (altura * altura)

    if resultado < 18.49:
            print(f"o seu IMC é:  {resultado} Você está baixo do peso")

    elif resultado < 24.99:
            print(f"o seu IMC é:  {resultado} Você está com o Peso normal")
    
    elif resultado < 29.99:
           print(f"o seu IMC é:  {resultado} Você está Acima do peso")
    
    elif resultado < 34.99:
           print(f"o seu IMC é:  {resultado} Você está com obesidade I")

    elif resultado < 39.99:
           print(f"o seu IMC é:  {resultado} Você está com obesidade II (severa)")
    else:
           print(f"o seu IMC é:  {resultado} Você está obesidade III (mórbida)")



inicio()