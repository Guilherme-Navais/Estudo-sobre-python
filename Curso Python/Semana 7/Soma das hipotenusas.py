def é_hipotenusa(n):
    i = 1
    j = 1
    zera_j = 1

    while i < n:
        while j < n:
            if (n**2) == (i**2 + j**2):
                return True
            else:
                j = j + 1
        
        i = i + 1
        j = zera_j
    
    return False


def soma_hipotenusas(n):
    contador = 1
    soma_das_hipotenusas = 0

    while contador <= n:
        if é_hipotenusa(contador) == True:
            soma_das_hipotenusas = soma_das_hipotenusas + contador
            contador = contador + 1
        else:
            contador = contador + 1
    
    return soma_das_hipotenusas