numero = int(input("Digite o valor de n: "))
contador = numero -1 

if numero == 0:
    numero = 1
else:
    while contador >= 1:
        numero = contador * numero
        contador = contador - 1

print(numero)