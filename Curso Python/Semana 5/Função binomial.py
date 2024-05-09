def fatorial(numero):
    contador = numero -1 

    if numero == 0:
        numero = 1
    else:
        while contador >= 1:
            numero = contador * numero
            contador = contador - 1
    
    return numero
            
n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

função_binomial = fatorial(n) / (fatorial(k) * fatorial(n - k))

print(função_binomial)