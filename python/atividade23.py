soma = 0
contador = 0

while True:
    num1 = float(input("digite um numero 0 para parar "))
    if num1 == 0:
        break
    soma += num1
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"a media dos numeros digitados é  {media}")

