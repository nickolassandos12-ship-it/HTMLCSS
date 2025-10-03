def inicio():
    print("vamos fazer a conversão de fahrenheit para celsius")
    print("para realizar esse calculo digite o valor em fahrenheit")

    num1 = float(input("digite o valor em fahrenheit \n"))

    celsius = (num1 - 32) * 5 / 9 

    print("esse é o calculo (60°F-32)×5/9")

    print(f"a conversão de {num1} fahrenheit para graus celsius é: {celsius}")
           
inicio()