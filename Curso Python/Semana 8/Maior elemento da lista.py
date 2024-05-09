def maior_elemento(lista):
    maior_numero = lista[0]

    for item in lista:
        if item > maior_numero:
            maior_numero = item
    
    return maior_numero

