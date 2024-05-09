def fatorial(numero):
    contador = numero -1 

    if numero == 0:
        numero = 1
    else:
        while contador >= 1:
            numero = contador * numero
            contador = contador - 1
    
    return numero

numero = int(input("Digite um número inteiro: " ))

while numero >= 0:
    print(fatorial(numero))
    numero = int(input("Digite um número inteiro: " ))