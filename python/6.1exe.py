import time
def inicio():
    codigo = 10
    secodigo = 0
                 
    secodigo = int(input("digite o código:"))
    if secodigo == codigo:
         print("parabens")
         return
    else:
        for numero in range(20, 0, -1):
            print(f"a bomba vai explodir em {numero}")
            time.sleep(1)
                
inicio()