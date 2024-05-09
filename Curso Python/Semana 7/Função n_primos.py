def n_primos(n):
    quantidade_de_primos = 0
    contador = 2

    while contador <= n:
        if éPrimo(contador) == True:
            quantidade_de_primos = quantidade_de_primos + 1
            contador = contador + 1
        else:
            contador = contador + 1
    
    return quantidade_de_primos


def éPrimo(num):
    contador = num
    divide = num
    primo = True

    while divide != 2:
        divide = contador - 1
        contador = contador - 1
        if num % divide == 0:
            divide = 2
            primo = False
    
    if not primo:
        return False
    else:
        return True