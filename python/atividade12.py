# Contador de negativos e positivos

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))
numero5 = float(input("Digite o quinto número: "))
numero6 = float(input("Digite o sexto número: "))
numero7 = float(input("Digite o sétimo número: "))
numero8 = float(input("Digite o oitavo número: "))

positivos = 0
negativos = 0

numeros = [numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8]

for n in numeros:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
