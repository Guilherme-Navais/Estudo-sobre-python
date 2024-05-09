def remove_repetidos(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    
    nova_lista.sort()

    return nova_lista



